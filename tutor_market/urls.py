from django.urls import path
from tutor_market import views

urlpatterns = [
    path('', views.TutorList.as_view(), name='tutor_list'),
    path('<int:pk>/', views.tutor_detail_view, name='tutor_detail'),
    path('add-tutor/', views.TutorCreateView.as_view(), name='add_tutor'),
    path('edit-tutor/<int:pk>/', views.TutorUpdateView.as_view(), name='edit_tutor'),
    path('delete-tutor/<int:pk>/', views.TutorDeleteView.as_view(), name='delete_tutor'),
]
