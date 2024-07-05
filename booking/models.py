from datetime import timedelta
from django.db import models


class TutoringSession(models.Model):
    # Genereal fields
    tutor = models.ForeignKey(
        "tutor_market.Tutor", on_delete=models.CASCADE, related_name="sessions"
    )
    student = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="sessions"
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    payment_complete = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=200, blank=True, null=True)
    subject = models.ForeignKey("tutor_market.Subject", on_delete=models.CASCADE, default=1)

    # Calendly json fields
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField()
    location_url = models.URLField()
    session_name = models.CharField(max_length=200)
    event_uri = models.CharField(
        max_length=200
    )  # Technically i could update the session periodically using the uri ... future feature
    invitee_uri = models.CharField(max_length=200)
    cancel_url = models.URLField()
    reschedule_url = models.URLField()
    invitee_email = models.EmailField()
    invitee_notes = models.TextField(blank=True, null=True)

    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
        ("rescheduled", "Rescheduled"),
    ]
    session_status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="scheduled"
    )

    def duration(self) -> timedelta:
        return self.end_time - self.start_time
