from django.urls import path
from core import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
]
