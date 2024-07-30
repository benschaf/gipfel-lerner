import base64
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.contrib import messages

from booking.views import _update_users_sessions
from core.models import FrequentlyAskedQuestion
from gipfel_tutor import settings


class LandingPageView(TemplateView):
    """
    A view that renders the landing page template.
    """
    template_name = 'core/index.html'


class AboutPageView(TemplateView):
    """
    A view that renders the about page template.
    """
    template_name = 'core/about.html'


class FAQPageView(ListView):
    model = FrequentlyAskedQuestion
    template_name = "core/faq.html"
    context_object_name = "faqs"
