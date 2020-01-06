from django.shortcuts import render
from .models import Tutorial
from django.views import generic
from django.shortcuts import render
# Create your views here.

class TutorialDetailView(generic.DetailView):
	model = Tutorial

def LevelFinish(request, pk):
	tutorial = Tutorial.objects.get(pk=pk)
	context = {'tutorial': tutorial, 'finished': True}
	return render(request, 'finish.html', context)