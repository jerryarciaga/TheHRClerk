from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.db import transaction

from .forms import SignUpForm, ProfileForm

@transaction.atomic
def signup(request):
    # Log any user out when trying to make an account
    if request.user is not None:
        logout(request)
    
    # Redirect to home if user successfully signs up
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            profile_form.save()
            return redirect('home:home')
    # Render the sign up form
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()
    return render(
        request = request,
        template_name = 'accounts/signup.html', 
        context = {
            'user_form' : user_form,
            'profile_form' : profile_form,
        }
    )

def userlogout(request):
    logout(request)
    return redirect('home:home')
