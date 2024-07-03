from django.shortcuts import render
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    """
    A view that renders the landing page template.
    """
    template_name = 'core/index.html'


class StudentOrTutorView(TemplateView):
    """
    A view that renders the 'student_or_tutor.html' template.
    """
    template_name = 'core/student_or_tutor.html'