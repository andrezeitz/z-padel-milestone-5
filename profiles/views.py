from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, 'profiles/profile.html', context)


@login_required
def admin_profile(request):
    """ Display the admin profile. """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    orders = Order.objects.all()

    context = {
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, 'profiles/admin.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
