
from django import forms

from booking.models import Payment


class CalendlyUriForm(forms.Form):
    event_uri = forms.URLField(label='Calendly Event URI', max_length=200)
    invitee_uri = forms.URLField(label='Calendly Invitee URI', max_length=200)


class PaymentForm(forms.ModelForm):
    sessions = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Payment
        exclude = []
