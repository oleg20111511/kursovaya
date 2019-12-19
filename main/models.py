from django.db import models
from django.urls import reverse

# Create your models here.

class TutorialTheme(models.Model):
	name = models.CharField(max_length=50, help_text='Тема обучалок', primary_key=True)

	def get_absolute_url(self):
		return reverse('tutorial-theme', args=[str(self.name)])

	def __str__(self):
		return self.name

class Tutorial(models.Model):
	name = models.CharField(max_length=50, help_text='Название обучалки')
	theme = models.ForeignKey('TutorialTheme', on_delete=models.CASCADE, null=True)
	background = models.ImageField(upload_to='img/')
	def __str__(self):
		return self.name

class LevelTheme(models.Model):
	name = models.CharField(max_length=50, help_text='Тема уровней', primary_key=True)
	background = models.ImageField(upload_to='img/')
	
	def get_absolute_url(self):
		return reverse('theme-levels', args=[str(self.name)])
	def get_list_url(self):
		return reverse('level-theme', args=[str(self.name)])

	def __str__(self):
		return self.name

class Level(models.Model):
	name = models.CharField(max_length=50, help_text='Название уровня')
	theme = models.ForeignKey('LevelTheme', on_delete=models.CASCADE, null=True)
	background = models.ImageField(upload_to='img/')
	def __str__(self):
		return self.name
	pass