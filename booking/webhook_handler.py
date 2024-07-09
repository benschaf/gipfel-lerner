from django.http import HttpRequest, HttpResponse


class StripeWH_Handler:

    def __init__(self, request: HttpRequest):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )