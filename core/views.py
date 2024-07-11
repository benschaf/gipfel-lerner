from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from booking.views import _update_users_sessions


class LandingPageView(TemplateView):
    """
    A view that renders the landing page template.
    """
    template_name = 'core/index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            _update_users_sessions(request.user)
        return super().get(request, *args, **kwargs)


class StudentOrTutorView(TemplateView):
    """
    A view that renders the 'student_or_tutor.html' template.
    """
    template_name = 'core/student_or_tutor.html'