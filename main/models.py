from django.db import models
from django.urls import reverse

# Create your models here.

class TutorialTheme(models.Model):
	name = models.CharField(max_length=50, primary_key=True, verbose_name='Тема обучалок:')

	def get_tutorials_amount(self):
		return self.tutorial_set.all().count()
	get_tutorials_amount.short_description = 'Количество обучалок:'
	def get_absolute_url(self):
		return reverse('tutorial-theme', args=[str(self.name)])
	def __str__(self):
		return self.name

class Tutorial(models.Model):
	name = models.CharField(max_length=50, verbose_name='Название обучалки:')
	theme = models.ForeignKey('TutorialTheme', on_delete=models.CASCADE, null=True, verbose_name='Тема:')
	background = models.ImageField(upload_to='img/', verbose_name='Фон:')
	def __str__(self):
		return self.name


class LevelTheme(models.Model):
	name = models.CharField(max_length=50, verbose_name='Тема уровней:', primary_key=True)
	background = models.ImageField(upload_to='img/', verbose_name='Фон:')
	
	def get_levels_amount(self):
		return self.level_set.all().count()
	get_levels_amount.short_description = 'Количество уровней:'
	def get_absolute_url(self):
		return reverse('theme-levels', args=[str(self.name)])
	def get_list_url(self):
		return reverse('level-theme', args=[str(self.name)])
	def __str__(self):
		return self.name

class Level(models.Model):
	name = models.CharField(max_length=50, verbose_name='Название уровня')
	theme = models.ForeignKey('LevelTheme', on_delete=models.CASCADE, null=True, verbose_name='Тема:')
	background = models.ImageField(upload_to='img/', verbose_name='Фон:')
	def __str__(self):
		return self.name
	pass