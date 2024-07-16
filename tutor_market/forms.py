from django import forms
from .models import Rating, Tutor, Subject


class TutorForm(forms.ModelForm):

    class Meta:
        model = Tutor
        fields = ['display_name', 'subjects', 'hourly_rate', 'values', 'catch_phrase',
                  'description', 'profile_image', 'iban', 'calendly_event_url', 'calendly_personal_token']

    def __init__(self, *args, **kwargs):
        super(TutorForm, self).__init__(*args, **kwargs)
        self.fields['display_name'].help_text = 'Enter the Name you would like your Students to see.'
        self.fields['subjects'].help_text = 'Select the subjects you teach. (Select Multiple by holding Ctrl / Command and clicking)'
        self.fields['hourly_rate'].help_text = 'Specify your hourly rate. For tutors just starting off €15 is recommended but it is completely up to you.'
        self.fields['values'].help_text = 'Pick the teaching values, that resonate with you the most.'
        self.fields['catch_phrase'].help_text = 'Enter a catchy phrase that represents you as a tutor. This is one of the first things students will see about you.'
        self.fields['description'].help_text = 'Provide a detailed description of your tutoring services.'
        self.fields['profile_image'].help_text = 'Upload your profile image.'
        self.fields['iban'].help_text = 'Enter your IBAN for payments we make to you after lessons.'
        self.fields['calendly_event_url'].help_text = 'Provide your Calendly event URL for scheduling sessions.'
        self.fields['calendly_personal_token'].help_text = 'Enter your Calendly personal token so we can schedule lessons for you.'


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['score', 'comment']
