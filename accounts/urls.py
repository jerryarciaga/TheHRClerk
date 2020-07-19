from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^profile/$', views.UserProfileView.as_view(), name='profile'),
    url(r'^update_user/$', views.UpdateUserView.as_view(), name='update_user'),
    url(r'^logout/$', views.userlogout, name='logout'),
]
