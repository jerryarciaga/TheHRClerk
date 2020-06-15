from django.shortcuts import render

def index(request):
    context = {
        'title': 'Awards Index',
    }
    return render(request, 'awards/awards_index.html')
