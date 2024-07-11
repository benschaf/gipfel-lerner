import time
from django.http import HttpResponse
from django.contrib import auth

from booking.models import Payment, TutoringSession


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        print("webhook received")
        intent = event.data.object
        session_ids = intent.metadata.sessions.split(",")



        max_attempts = 3
        delay_between_attempts = 2  # seconds

        for attempt in range(max_attempts):
            try:
                payment = Payment.objects.get(
                    stripe_id=intent.id,
                )
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified payment already in database',
                    status=200,
                )
            except Payment.DoesNotExist:
                print(f"Attempt {attempt + 1}: Payment does not exist. Retrying...")
                if attempt < max_attempts - 1:
                    time.sleep(delay_between_attempts)
                else:
                    user = auth.User.objects.get(id=intent.metadata.user_id)
                    try:
                        payment = Payment.objects.create(
                            user=user,
                            amount=intent.amount,
                            status="succeeded",
                            client_secret=intent.client_secret,
                            currency=intent.currency,
                            stripe_id=intent.id,
                        )

                        # Update the payment_complete field of the sessions
                        sessions_to_pay = TutoringSession.objects.filter(pk__in=session_ids)

                        for session in sessions_to_pay:
                            session.payment_complete = True
                            session.payment = self.object
                            session.save()

                    except Exception as e:
                        if payment:
                            payment.delete()
                        return HttpResponse(
                            content=f'Webhook received: {event["type"]} | ERROR: {e}',
                            status=500,
                        )
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | SUCCESS: Payment does not exist after {max_attempts} attempts - created new payment in database',
                        status=200,
                    )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)
