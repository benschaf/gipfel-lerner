from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from tutor_market.forms import TutorForm
from tutor_market.models import Tutor


class TutorList(ListView):
    """
    View for listing all tutors in the system.
    """
    model = Tutor
    template_name = 'tutor_market/tutor_list.html'
    context_object_name = 'tutor_list'
    paginate_by = 6


class TutorDetailView(DetailView):
    """
    View for displaying the details (Profile) of a tutor.
    """
    model = Tutor
    template_name = 'tutor_market/tutor_detail.html'
    context_object_name = 'tutor'


class TutorCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new tutor profile.
    """

    model = Tutor
    form_class = TutorForm
    template_name = 'tutor_market/add_tutor.html'

    def form_valid(self, form):
        """
        Checks if the current user already has a Tutor instance and if so,
        redirects to the tutor's detail page.

        Sets the user field of the form instance to the current user.
        """
        if Tutor.objects.filter(user=self.request.user).exists():
            messages.error(self.request, 'You already have a tutor profile.')
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

    def test_func(self):
        """
        Checks if the current user is the owner of the tutor object.
        """
        if self.request.user == self.get_object().user:
            return True

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

    def test_func(self):
        """
        Checks if the current user is the owner of the tutor Profile.
        """
        if self.request.user == self.get_object().user:
            return True
