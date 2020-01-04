from django.shortcuts import render
from .models import Tutorial
from django.views import generic
# Create your views here.

class TutorialDetailView(generic.DetailView):
	model = Tutorial