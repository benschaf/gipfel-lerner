from django.urls import path
from tutor_market import views

urlpatterns = [
    path('', views.TutorList.as_view(), name='tutor_list'),
]
