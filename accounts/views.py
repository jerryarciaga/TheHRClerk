from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup(request):
    # Log any user out when trying to make an account
    if request.user.is_authenticated:
        logout(request)
    
    # Redirect to home if user successfully signs up
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:home')
    # Render the sign up form
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form' : form})

def userlogout(request):
    logout(request)
    return redirect('home:home')
