from django.conf.urls import url,include
from re_login.views import register,login
urlpatterns = [
    url(r'^$',login),
    url(r'^login/', login),
    url(r'^register/', register),
]