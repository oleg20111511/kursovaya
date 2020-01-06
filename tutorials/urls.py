from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^(?P<pk>\w+)$', views.TutorialDetailView.as_view(), name='tutorial'),
	url(r'^(?P<pk>\w+)/finish$', views.TutorialFinish, name='tutorial-finish')
]