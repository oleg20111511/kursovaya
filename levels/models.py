from django.db import models
from django.urls import reverse

# Create your models here.

class Level(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Question(models.Model):
	name = models.CharField(max_length=100)
	level = models.ForeignKey('Level', on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return self.name