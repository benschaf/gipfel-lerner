from django.contrib import admin

from booking.models import Payment, TutoringSession

# Register your models here.
admin.site.register(TutoringSession)
admin.site.register(Payment)

