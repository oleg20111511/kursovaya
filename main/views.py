from django.shortcuts import render
from .models import TutorialThemeTheme, TutorialTheme, Tutorial, LevelThemeTheme, LevelTheme, Level
from django.views import generic
# Create your views here.

tutorial_themes = TutorialTheme.objects.all()

def index(request):
	return render(request, 'index.html', context={'tutorial_themes': tutorial_themes})

class TutorialThemeThemeDetailView(generic.DetailView):
	model = TutorialThemeTheme
	template_name = 'list_template.html'
	def get_context_data(self, **kwargs):
		context = super(TutorialThemeThemeDetailView, self).get_context_data(**kwargs)
		object_list = self.object.tutorialtheme_set.all()
		context['object_list'] = object_list
		return context

class TutorialThemeDetailView(generic.DetailView):
	model = TutorialTheme
	template_name = 'list_template.html'
	def get_context_data(self, **kwargs):
		context = super(TutorialThemeDetailView, self).get_context_data(**kwargs)
		object_list = self.object.tutorial_set.all()
		context['object_list'] = object_list
		return context

class LevelThemeThemeDetailView(generic.DetailView):
	model = LevelThemeTheme
	template_name = 'list_template.html'
	def get_context_data(self, **kwargs):
		context = super(LevelThemeThemeDetailView, self).get_context_data(**kwargs)
		object_list = self.object.leveltheme_set.all()
		context['object_list'] = object_list
		return context

class LevelThemeDetailView(generic.DetailView):
	model = LevelTheme
	template_name = 'list_template.html'
	def get_context_data(self, **kwargs):
		context = super(LevelThemeDetailView, self).get_context_data(**kwargs)
		object_list = self.object.level_set.all()
		context['object_list'] = object_list
		return context