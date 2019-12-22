from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^(?P<pk>\w+)$', views.LevelDetailView.as_view(), name='level')
]