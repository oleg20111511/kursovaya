from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^tutorials/(?P<pk>\w+)$', views.TutorialThemeDetailView.as_view(), name='tutorial-theme'),
	url(r'^levels/$', views.LevelThemeListView.as_view(), name='level-theme'),
	url(r'^levels/(?P<pk>\w+)$', views.LevelThemeDetailView.as_view(), name='theme-levels')
]