from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from django.views import View
from django.utils.decorators import method_decorator
from django.db import transaction

from .forms import SignUpForm, ProfileForm

class SignUpView(View):
    """Renders a Sign Up view on GET and creates a user on POST """
    user_form = SignUpForm
    profile_form = ProfileForm
    template_name = 'accounts/signup.html'
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }

    def get(self, request, *args, **kwargs):
        """
        Log any user out, then render SignUpForm
        """
        if request.user is not None:
            logout(request)
        user_form = self.user_form()
        profile_form = self.profile_form()
        return render(
            request,
            template_name = self.template_name,
            context = self.context,
        )
    
    @method_decorator(transaction.atomic)
    def post(self, request, *args, **kwargs):
        """
        Save user info when the Sign Up button is pressed. Validate the data,
        checking for any errors. If valid, log the user in then update the
        user with data from the Profile Form.
        """
        user_form = self.user_form(request.POST)
        profile_form = self.profile_form(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            profile_form = self.profile_form(request.POST, instance=request.user.profile)
            profile_form.save()
            return redirect('home:home')


def userlogout(request):
    """Log the current user out, then redirect to the home page."""
    logout(request)
    return redirect('home:home')
