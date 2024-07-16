from django import forms
from .models import Rating, Tutor, Subject


class TutorForm(forms.ModelForm):

    class Meta:
        model = Tutor
        fields = ['display_name', 'subjects', 'hourly_rate', 'values', 'catch_phrase',
                  'description', 'profile_image', 'iban', 'calendly_event_url', 'calendly_personal_token']


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['score', 'comment']
