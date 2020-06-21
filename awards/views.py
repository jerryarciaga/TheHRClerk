from django.shortcuts import render

def home(request):
    return render(request, 'awards/home.html')
