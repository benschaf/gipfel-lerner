from django.shortcuts import render
from django.views.generic import ListView, DetailView

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
    model = Tutor
    template_name = 'tutor_market/tutor_detail.html'
    context_object_name = 'tutor'