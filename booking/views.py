import json
from typing import Any
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
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

def _get_json_from_calendly_uri(uri):
    headers = {'Authorization': f'Bearer {settings.PERSONAL_CALENDLY_TOKEN}'}
    response = requests.get(uri, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error
        print(f"error: {response.status_code}")


def _write_calendly_data_to_db(event_data, invitee_data, tutor, student):
    # Create a new session
    print(f"EVENT_DATA: {event_data}")
    print(f"INVITEE_DATA: {invitee_data}")

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
        event_uri = form.cleaned_data['event_uri']
        invitee_uri = form.cleaned_data['invitee_uri']
        event_data = _get_json_from_calendly_uri(event_uri)
        invitee_data = _get_json_from_calendly_uri(invitee_uri)

        session = _write_calendly_data_to_db(event_data, invitee_data, tutor, student)

    return redirect('schedule_success', pk=session.pk)


class ScheduleSuccessView(DetailView):
    model = TutoringSession
    template_name = 'booking/schedule_success.html'
    context_object_name = 'session'


def payment_view(request, pk):
    """
    View for handling the payment of a tutoring session.
    """
    sessions_to_pay = TutoringSession.objects.filter(student=request.user, payment_complete=False)

    if not sessions_to_pay:
        messages.error(request, 'No sessions to pay for.')
        return redirect('dashboard')

    total_price = round(sum([session.price for session in sessions_to_pay]))

    STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=total_price,
        currency=settings.STRIPE_CURRENCY,
    )
    CLIENT_SECRET = intent.client_secret

    print(f"intent {intent}")


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

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        # update the sessions
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('payment_success', kwargs={'pk': self.object.pk})





