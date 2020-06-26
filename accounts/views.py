from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form' : form})

def userlogin(request):
    return render(request, 'accounts/login.html')

def userlogout(request):
    logout(request)
    return redirect('home:home')
