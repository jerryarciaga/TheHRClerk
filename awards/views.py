from django.shortcuts import render

def index(request):
    return render(request, 'awards/awards_index.html')
