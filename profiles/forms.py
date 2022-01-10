from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_name': 'Full Name',
            'default_phone_number': 'Phone Number',
            'default_street_address': 'Street Address ',
            'default_postcode': 'Postal Code',
            'default_city': 'City',
        }

        self.fields['default_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = False