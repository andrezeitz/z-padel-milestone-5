from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for making the order in checkout
    """
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address',
            'city',
            'postcode',
        )