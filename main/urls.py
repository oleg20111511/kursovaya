from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import ListView, DetailView

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^tutorials/$', ListView.as_view(model=views.TutorialThemeTheme, template_name='list_template.html'), name='tutorial-theme-theme-list'),
	url(r'^tutorials/(?P<pk>\w+)$', views.TutorialThemeThemeDetailView.as_view(), name='tutorial-theme-theme-detail'),
	url(r'^tutorials/(?P<theme>\w+)/(?P<pk>\w+)$', views.TutorialThemeDetailView.as_view(), name='tutorial-theme'),
	url(r'^levels/$', ListView.as_view(model=views.LevelThemeTheme, template_name='list_template.html'), name='level-theme-theme-list'),
	url(r'^levels/(?P<pk>\w+)$', views.LevelThemeThemeDetailView.as_view(), name='level-theme-theme-detail'),
	url(r'^levels/(?P<theme>\w+)/(?P<pk>\w+)$', views.LevelThemeDetailView.as_view(), name='level-theme')
]