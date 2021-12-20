from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_SHIPPING:
        delivery = 10
    else:
        delivery = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_shipping': settings.FREE_SHIPPING,
        'grand_total': grand_total,
    }

    return context 