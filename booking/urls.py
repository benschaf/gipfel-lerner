from django.urls import path
from booking import views

urlpatterns = [
    path('fetch-calendly-data/<int:pk>/', views.fetch_calendly_data_view, name='fetch_calendly_data'),
    path('schedule-success/<int:pk>/', views.ScheduleSuccessView.as_view(), name='schedule_success'),
]
