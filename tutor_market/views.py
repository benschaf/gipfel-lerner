import json
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from typing import Any
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Count, Avg



from booking.forms import CalendlyUriForm
from booking.models import Payment, TutoringSession
from gipfel_tutor import settings
from tutor_market.forms import RatingForm, TutorForm
from tutor_market.models import Subject, Tutor, Rating
import requests
from django.urls import reverse_lazy


def tutor_list_view(request):
    """
    Function-based view for listing all tutors in the system.
    """
    tutor_list = Tutor.objects.all()
    subjects= None
    values = None
    query = None
    sorting = None

    if request.GET:
        if 'subject' in request.GET:
            subjects = request.GET.getlist('subject')
            q_arguments = Q()
            for subject in subjects:
                q_arguments |= Q(subjects__name__icontains=subject)
            tutor_list = tutor_list.filter(q_arguments).distinct()

        if 'teaching-value' in request.GET:
            # -> Credit for getting values from a list of query parameters: https://docs.djangoproject.com/en/5.0/ref/request-response/#querydict-objects
            values = request.GET.getlist('teaching-value')
            q_arguments = Q()
            for value in values:
                # -> Credit for |= operator: https://docs.djangoproject.com/en/5.0/ref/models/querysets/#or
                q_arguments |= Q(values__name__icontains=value)
            tutor_list = tutor_list.filter(q_arguments).distinct()

        if 'q' in request.GET:
            query = request.GET['q']

            queries = Q(display_name__icontains=query) | Q(description__icontains=query) | Q(catch_phrase__icontains=query) | Q(subjects__name__icontains=query) | Q(values__name__icontains=query)
            # -> Credit for returning distinct results: https://docs.djangoproject.com/en/5.0/ref/models/querysets/#distinct  # noqa
            tutor_list = tutor_list.filter(queries).distinct()

        if 'sorting' in request.GET:
            sorting = request.GET['sorting']
            if sorting == 'name':
                tutor_list = tutor_list.order_by('display_name')
            if sorting == 'cheapest':
                tutor_list = tutor_list.order_by('hourly_rate')
            if sorting == 'highest-rated':
                tutor_list = tutor_list.annotate(avg_rating=Avg('ratings__score')).order_by('-avg_rating')
            if sorting == 'most-reviews':
                tutor_list = tutor_list.annotate(num_reviews=Count('ratings')).order_by('-num_reviews')
            if sorting == 'most-expensive':
                tutor_list = tutor_list.order_by('-hourly_rate')

    # Pagination
    paginator = Paginator(tutor_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_term': query,
        'subjects': subjects,
        'values': values,
        'query': query,
        'sorting': sorting,
        'tutor_list': tutor_list,
    }
    return render(request, 'tutor_market/tutor_list.html', context)



def tutor_detail_view(request, pk):
    """
    View for displaying the details (Profile) of a tutor.
    If a POST request is made, a new review is added to the tutor's profile.
    """
    tutor = get_object_or_404(Tutor, pk=pk)
    existing_rating = None
    upcoming_sessions = None

    if request.user.is_authenticated:
        existing_rating = Rating.objects.filter(tutor=tutor, user=request.user).first()
        upcoming_sessions = TutoringSession.objects.filter(tutor__user=tutor.user, student=request.user)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, 'You must be logged in to leave a review.')
            return redirect('tutor_detail', pk=pk)

        review_form = RatingForm(request.POST)

        # how do I do proper form validation?
        # If I do it witha CBV the invalid form will reload the page and add
        # a specific error message on the invalid fields.
        if not review_form.is_valid():
            messages.warning(request, 'Form was not valid. Please try again.')

        # Update the old review and reload the view
        if existing_rating:
            existing_rating.score = review_form.cleaned_data['score']
            existing_rating.comment = review_form.cleaned_data['comment']
            existing_rating.save()
            messages.success(request, 'Review updated successfully.')
            return redirect('tutor_detail', pk=pk)

        review = review_form.save(commit=False)
        review.tutor = tutor
        review.user = request.user
        review.save()
        messages.success(request, 'Review added successfully.')
        return redirect('tutor_detail', pk=pk)

    form = RatingForm()
    calendly_form = CalendlyUriForm()
    calendly_event_url = tutor.calendly_event_url
    reviews = tutor.ratings.all()
    rating_exists = True if existing_rating else False
    context = {
        'tutor': tutor,
        'form': form,
        'calendly_form': calendly_form,
        'calendly_event_url': calendly_event_url,
        'reviews': reviews,
        'existing_review': rating_exists,
        'upcoming_sessions': upcoming_sessions,
    }
    return render(request, 'tutor_market/tutor_detail.html', context)


class TutorCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new tutor profile.
    """

    model = Tutor
    form_class = TutorForm
    template_name = 'tutor_market/add_tutor.html'
    success_message = 'Tutor profile created successfully.'

    def form_valid(self, form):
        """
        Checks if the current user already has a Tutor instance and if so,
        redirects to the tutor's detail page.

        Sets the user field of the form instance to the current user.
        """
        if Tutor.objects.filter(user=self.request.user).exists():
            messages.warning(self.request, 'You already have a tutor profile.')
            return redirect('tutor_detail', pk=self.request.user.tutor.pk)

        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        Builds the URL to the newly created tutor's detail page.
        """
        return reverse('tutor_detail', kwargs={'pk': self.object.pk})


class TutorUpdateView(UserPassesTestMixin, UpdateView):
    """
    A view for updating a tutor's information.
    """

    model = Tutor
    form_class = TutorForm
    template_name = 'tutor_market/edit_tutor.html'
    permission_required = 'tutor_market.change_tutor'
    success_message = 'Tutor profile updated successfully.'

    def test_func(self):
        """
        Checks if the current user is the owner of the tutor object.
        """
        if self.request.user == self.get_object().user:
            return True
        else:
            messages.warning(self.request, 'You do not have permission to update this profile.')
            return False

    def get_success_url(self):
        """
        Builds the URL to the updated tutor's detail page.
        """
        return reverse('tutor_detail', kwargs={'pk': self.object.pk})


class TutorDeleteView(UserPassesTestMixin, DeleteView):
    """
    A view for deleting a tutor.
    I wonder if tutors should be able to delete their profiles?...
    Maybe that just reverts them to being a student?
    """

    model = Tutor
    template_name = 'tutor_market/tutor_confirm_delete.html'
    permission_required = 'tutor_market.delete_tutor'
    success_url = reverse_lazy('tutor_list')
    success_message = 'Tutor profile deleted successfully.'

    def test_func(self):
        """
        Checks if the current user is the owner of the tutor Profile.
        """
        if self.request.user == self.get_object().user:
            return True
        else:
            messages.warning(self.request, 'You do not have permission to delete this profile.')
            return False


def student_dashboard(request, user):
    """
    View for displaying the student's dashboard.
    """
    booking_history = TutoringSession.objects.filter(student=user)
    # -> Credit for greater or equal to lookup (gte): https://docs.djangoproject.com/en/5.0/ref/models/querysets/#gte
    upcoming_sessions = booking_history.filter(start_time__gte=timezone.now())
    # add payment details (future feature)
    # add liked tutors (future feature)
    payment_history = Payment.objects.filter(user=user)
    context = {
        'upcoming_sessions': upcoming_sessions,
        'booking_history': booking_history,
        'payment_history': payment_history,
    }
    return render(request, 'tutor_market/student_dashboard.html', context)

def tutor_dashboard(request, user):
    """
    View for displaying the tutors's dashboard.
    """
    tutor = Tutor.objects.get(user=user)
    booking_history = TutoringSession.objects.filter(tutor=tutor).order_by('start_time')
    upcoming_sessions = booking_history.filter(start_time__gte=timezone.now()).filter(session_status='scheduled')[:3]
    pending_sessions = booking_history.filter(session_status='pending')
    users = User.objects.filter(sessions__tutor=tutor)
    users_and_sessions = {}
    for user in users:
        sessions = booking_history.filter(student=user)
        users_and_sessions[user] = sessions

    context = {
        'booking_history': booking_history,
        'pending_sessions': pending_sessions,
        'upcoming_sessions': upcoming_sessions,
        'users_and_sessions': users_and_sessions,
        'tutor': tutor,
    }
    return render(request, 'tutor_market/tutor_dashboard.html', context)

def dashboard_view(request, pk):
    """
    Redirects to the correct dashboard based on the user's role.
    """
    # CAN I DO THIS WEIRD VIEW THAT IS ONLY HALF A VIEW AND REDIRECTS TO THE APPROPRIATE SECOND HALF?
    user = get_object_or_404(User, pk=pk)
    connected_tutor_profile = Tutor.objects.filter(user=user).first()
    # connected_tutor_profile = False
    if connected_tutor_profile:
        return tutor_dashboard(request, user)
    else:
        return student_dashboard(request, user)

@require_POST
@login_required
def update_session_status(request, pk):
    """
    View for updating the status of a tutoring session.
    """
    session = get_object_or_404(TutoringSession, pk=pk)

    if session.tutor.user != request.user:
        messages.warning(request, 'You do not have permission to update this session.')
        return redirect('dashboard', pk=session.tutor.user.pk)

    session.session_status = request.POST['status']
    session.save()
    messages.success(request, 'Session status updated successfully.')
    return redirect('dashboard', pk=session.tutor.user.pk)


class CalendlyInformationView(TemplateView):
    template_name = 'tutor_market/calendly_information.html'