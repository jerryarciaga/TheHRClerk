from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.userlogin, name='login'),
    url('^logout/$', views.userlogout, name='logout'),
]
