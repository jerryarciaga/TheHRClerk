from django.conf.urls import url
from . import views

app_name = 'awards'
urlpatterns = [
    url(r'^$', views.AwardsHome.as_view(), name='home'),
]
