from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

class SignUpForm(UserCreationForm):
    """ Contains basic user information (username, email, etc). """
    first_name = forms.CharField(
        label = 'First Name',
        max_length = 30,
        required = True,
    )
    last_name = forms.CharField(
        label = 'Last Name',
        max_length = 30,
        required = True,
    )
    email = forms.EmailField(
        max_length = 254,
        help_text = 'Enter a valid email address.',
        required = True,
    )

    class Meta:
        """ Specifies the user form fields to fill out. """
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

class ProfileForm(forms.ModelForm):
    """ 
    This is an extension of the basic user info to fill out.
    Includes the user's rank and unit.
    """
    rank = forms.CharField(
        label = 'Rank',
        max_length = 3,
        help_text = 'Enter your abbreviated military rank.',
        required = True,
    )
    unit = forms.CharField(
        label = 'Unit',
        max_length = 50,
        help_text = 'Enter Unit Name, starting from Company/Troop/Battery',
        required = True,
    )

    class Meta:
        """ Specifies the form fields for additional User info. """
        model = Profile
        fields = (
            'rank',
            'unit',
        )
