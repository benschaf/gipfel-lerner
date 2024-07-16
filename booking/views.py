import json
from typing import Any
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
import requests
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView
from django.contrib import messages
from django.contrib.auth.models import User

from booking.forms import CalendlyUriForm, PaymentForm
from booking.models import Payment, TutoringSession
from gipfel_tutor import settings
from tutor_market.models import Tutor
import stripe

@require_POST
def cache_payment_data(request):
    print('reached the view')
    try:
        payment_intent_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session_id_string = request.POST.get('sessions')
        user_id = request.POST.get('user')
        stripe.PaymentIntent.modify(payment_intent_id, metadata={
            'user_id': user_id,
            'sessions': session_id_string,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.warning(request, 'An error occurred while processing your payment.')
        return HttpResponse(content=e, status=400)

def _get_json_from_calendly_uri(uri, tutor, request):
    calendly_personal_token = tutor.calendly_personal_token.strip()
    print(calendly_personal_token)
    headers = {'Authorization': f'Bearer {calendly_personal_token}'}
    response = requests.get(uri, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        if request:
            messages.warning(request, f'An error occured while loading the event data. ${response}')
        return None


def _write_calendly_data_to_db(event_data, invitee_data, tutor, student, request):
    # Create a new session

    questions_and_answers = ''
    if invitee_data['resource']['questions_and_answers']:
        questions_and_answers = invitee_data['resource']['questions_and_answers'][0]['answer']

    session = TutoringSession.objects.create(
        tutor=tutor,
        student=student,
        price = tutor.hourly_rate,
        # Subject is left to its default (other) for now

        # Calendly json fields
        start_time = event_data['resource']['start_time'],
        end_time = event_data['resource']['end_time'],
        created_at = event_data['resource']['created_at'],
        location_url = event_data['resource']['location']['join_url'],
        session_name = event_data['resource']['name'],
        event_uri = event_data['resource']['uri'],
        invitee_uri = invitee_data['resource']['uri'],
        cancel_url = invitee_data['resource']['cancel_url'],
        reschedule_url = invitee_data['resource']['reschedule_url'],
        invitee_email = invitee_data['resource']['email'],
        invitee_notes = questions_and_answers
    )
    session.save()
    messages.success(request, 'Session created successfully.')
    return session

@login_required
def fetch_calendly_data_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    View for fetching and displaying the tutor's Calendly data.
    """
    if not request.method == 'POST':
        return redirect('tutor_detail', pk=pk)

    tutor = get_object_or_404(Tutor, pk=pk)
    student = request.user

    form = CalendlyUriForm(request.POST)
    if form.is_valid():
        # get the uris
        event_uri = form.cleaned_data['event_uri']
        invitee_uri = form.cleaned_data['invitee_uri']

        #get the data from the uris using the calendly api2
        event_data = _get_json_from_calendly_uri(event_uri, tutor, request)
        invitee_data = _get_json_from_calendly_uri(invitee_uri, tutor, request)

        session = _write_calendly_data_to_db(event_data, invitee_data, tutor, student, request)

    return redirect('schedule_success', pk=session.pk)


def _update_users_sessions(user: User):
    """
    function that gets called periodically to update the user's sessions from their
    calendly data.
    """
    sessions_to_update = []
    tutor = None
    if Tutor.objects.filter(user=user).exists():
        tutor = Tutor.objects.filter(user=user)
        print('User is a tutor')
        sessions_to_update = TutoringSession.objects.filter(tutor__user=user)
    else:
        print('User is a student')
        sessions_to_update = TutoringSession.objects.filter(student=user)

    for session in sessions_to_update:
        try:
            event_data = _get_json_from_calendly_uri(session.event_uri, tutor, None)
            invitee_data = _get_json_from_calendly_uri(session.invitee_uri, tutor, None)

            # Calendly json fields
            session.start_time = event_data['resource']['start_time']
            session.end_time = event_data['resource']['end_time']
            session.location_url = event_data['resource']['location']['join_url']
            session.session_name = event_data['resource']['name']
            session.cancel_url = invitee_data['resource']['cancel_url']
            session.reschedule_url = invitee_data['resource']['reschedule_url']
            session.invitee_email = invitee_data['resource']['email']

            session.save()
            print(f"Session {session.pk} updated.")
        except Exception as e:
            print(f"Error updating session {session.pk}: {e}")


class ScheduleSuccessView(DetailView):
    model = TutoringSession
    template_name = 'booking/schedule_success.html'
    context_object_name = 'session'


@login_required
def payment_view(request, pk):
    """
    View for handling the payment of a tutoring session.
    """
    sessions_to_pay = TutoringSession.objects.filter(student=request.user, payment_complete=False)

    if not sessions_to_pay:
        messages.warning(request, 'No sessions to pay for.')
        return redirect('dashboard')

    total_price = round(sum([session.price for session in sessions_to_pay]))

    STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=total_price,
        currency=settings.STRIPE_CURRENCY,
    )
    CLIENT_SECRET = intent.client_secret

    context = {
        'sessions': sessions_to_pay,
        'total_price': total_price,
        'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_KEY,
        'CLIENT_SECRET': CLIENT_SECRET,
    }
    return render(request, 'booking/payment.html', context)


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'booking/payment_create.html'
    success_message = 'Payment successful.'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)

        # update the sessions
        session_ids = form.cleaned_data['sessions'].split(',')
        sessions_to_pay = TutoringSession.objects.filter(pk__in=session_ids)

        for session in sessions_to_pay:
            session.payment_complete = True
            session.payment = self.object
            session.save()

        return response

    def get_success_url(self) -> str:
        return reverse('payment_success', kwargs={'pk': self.object.pk})



class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'booking/payment_success.html'
    context_object_name = 'payment'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['sessions'] = TutoringSession.objects.filter(payment=self.object)
        return context