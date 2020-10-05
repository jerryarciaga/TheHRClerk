from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views import View

class ActionsHome(View):
    """ Renders a home view for the Actions WebApp """
    template_name = 'actions/home.html'
    
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(
            request,
            template_name = self.template_name,
        )
