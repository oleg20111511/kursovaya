from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^(?P<pk>\w+)$', views.LevelDetailView.as_view(), name='level'),
	url(r'^(?P<pk>\w+)/saveres$', views.SaveScoreView, name='save_score'),
	url(r'^(?P<pk>\w+)/finish$', views.LevelFinish, name='level-finish')
]