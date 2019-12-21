from django.shortcuts import render
from django.conf import settings
from .models import TutorialTheme, Tutorial, LevelTheme, Level
from django.views import generic
import os
# Create your views here.

def index(request):
	tutorial_themes = TutorialTheme.objects.all()

	return render(request, 'index.html', context={'tutorial_themes': tutorial_themes})

class TutorialThemeDetailView(generic.DetailView):
	model = TutorialTheme
	tutorial_themes = TutorialTheme.objects.all()

	def get_context_data(self, **kwargs):
		context = super(TutorialThemeDetailView, self).get_context_data(**kwargs)
		context['tutorial_themes'] = self.tutorial_themes
		return context

class LevelThemeDetailView(generic.DetailView):
	model = LevelTheme
	tutorial_themes = TutorialTheme.objects.all()

	def get_context_data(self, **kwargs):
		context = super(LevelThemeDetailView, self).get_context_data(**kwargs)
		context['tutorial_themes'] = self.tutorial_themes
		return context

class LevelThemeListView(generic.ListView):
	model = LevelTheme
	tutorial_themes = TutorialTheme.objects.all()

	def get_context_data(self, **kwargs):
		context = super(LevelThemeListView, self).get_context_data(**kwargs)
		context['tutorial_themes'] = self.tutorial_themes
		return context