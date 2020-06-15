from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.index, name='awards_home'),
=======
    url(r'^$', views.home, name='awards_home'),
>>>>>>> 59f2f20cbb99bef25ba26902bbbf320770454e54
]
