from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views import View

class AwardsHome(View):
    """ Renders a home view for the Awards WebApp """
    template_name = 'awards/home.html'
    
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(
            request,
            template_name = self.template_name,
        )
