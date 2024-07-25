import base64
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages

from booking.views import _update_users_sessions
from gipfel_tutor import settings


class LandingPageView(TemplateView):
    """
    A view that renders the landing page template.
    """
    template_name = 'core/index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            pass
            # need to find a better place to update the sessions in the background
            # _update_users_sessions(request.user)
        return super().get(request, *args, **kwargs)

