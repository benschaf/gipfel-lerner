from django.shortcuts import render
from django.views.generic import ListView

from tutor_market.models import Tutor


class TutorList(ListView):
    """
    View for listing all tutors in the system.
    """
    model = Tutor
    template_name = 'tutor_market/tutor_list.html'
    paginate_by = 6