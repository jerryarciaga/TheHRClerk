from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="First Name",
        max_length=30,
        required=True,
        )
    last_name = forms.CharField(
        label="Last Name",
        max_length=30,
        required=True,
        )
    email = forms.EmailField(
        max_length=254,
        help_text='Enter a valid email address.',
        required=True,
        )

    class Meta:
        model = User
        fields = (
                'username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
                )
