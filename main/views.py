from django.shortcuts import render
from .models import TutorialTheme, LevelThemeTheme, LevelTheme
from django.views import generic
from django.http import JsonResponse
# Create your views here.

def index(request):
	return render(request, 'index.html')

# class TutorialThemeThemeDetailView(generic.DetailView):
# 	model = TutorialThemeTheme
# 	template_name = 'list_template.html'
# 	def get_context_data(self, **kwargs):
# 		context = super(TutorialThemeThemeDetailView, self).get_context_data(**kwargs)
# 		object_list = self.object.tutorialtheme_set.all()
# 		context['object_list'] = object_list
# 		return context

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