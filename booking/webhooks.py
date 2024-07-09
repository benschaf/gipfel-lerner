import json
import os
import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from gipfel_tutor import settings

stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret = settings.STRIPE_WEBHOOK_SECRET


@csrf_exempt
def webhook(request):
    event = None

    try:
        event = json.loads(request.body)
    except json.decoder.JSONDecodeError as e:
        print('⚠️  Webhook error while parsing basic request.' + str(e))
        return JsonResponse({'success': False}, status=400)

    if endpoint_secret:
        sig_header = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                request.body, sig_header, endpoint_secret
            )
        except stripe.error.SignatureVerificationError as e:
            print('⚠️  Webhook signature verification failed.' + str(e))
            return JsonResponse({'success': False}, status=400)

    # Handle the event
    if event and event['type'] == 'payment_intent.succeeded':
        # contains a stripe.PaymentIntent
        payment_intent = event['data']['object']
        print('Payment for {} succeeded'.format(payment_intent['amount']))
        # Then define and call a method to handle the successful payment intent.
        # handle_payment_intent_succeeded(payment_intent)
    elif event['type'] == 'payment_intent.payment_failed':
        payment_intent = event['data']['object']
        print('Payment for {} failed'.format(payment_intent['amount']))
    elif event['type'] == 'payment_intent.processing':
        payment_intent = event['data']['object']
        print('Payment for {} processing'.format(payment_intent['amount']))
    else:
        # Unexpected event type
        print('Unhandled event type {}'.format(event['type']))

    return JsonResponse({'success': True})
