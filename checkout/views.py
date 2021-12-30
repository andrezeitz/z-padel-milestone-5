from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('home'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K2DWxGe8uuVxA1CsDfuKUoW69GTg2LQMecgkntCZKtEVHApPvPnmaFeOLCW9V09cZhFEC6Tqfa4N24F1ywE2F7W00XNp175JP',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

