from django.shortcuts import render
from .models import Level, Question, Answer
from django.views import generic
# Create your views here.

class LevelDetailView(generic.DetailView):
	model = Level