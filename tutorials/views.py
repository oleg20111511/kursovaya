from django.shortcuts import render
from main.models import Level
from main.models import Tutorial as TutorialLink
from .models import Tutorial
from django.views import generic
from django.shortcuts import render
# Create your views here.

class TutorialDetailView(generic.DetailView):
	model = Tutorial

def TutorialFinish(request, pk):
	tutorial = TutorialLink.objects.get(name=pk)
	level = Level.objects.get(name=tutorial.name)
	image = level.background.url
	context = {'tutorial': tutorial, 'image': image, 'finished': True}
	return render(request, 'finish.html', context)