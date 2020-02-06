from django.urls import path
from . import views
from django.conf.urls import url



urlpatterns = [
	url(r'^register/$', views.MyRegisterFormView.as_view(), name='register'),
	url(r'^account/(?P<pk>\w+)$', views.ProfilePage, name='profile')
]