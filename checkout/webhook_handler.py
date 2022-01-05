from django.http import HttpResponse


class StripeWH_Handler:
    "Stripe webhook"

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Will handle a unexpected webook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )    