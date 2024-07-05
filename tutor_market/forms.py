from django import forms
from .models import Rating, Tutor, Subject

class TutorForm(forms.ModelForm):

    class Meta:
        model = Tutor
        fields = ['display_name', 'subjects', 'hourly_rate', 'values', 'catch_phrase', 'description', 'profile_image']


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['score', 'comment']


class CalendlyUriForm(forms.Form):
    event_uri = forms.URLField(label='Calendly Event URI', max_length=200)
    invitee_uri = forms.URLField(label='Calendly Invitee URI', max_length=200)


