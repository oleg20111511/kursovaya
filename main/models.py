from django.db import models
from django.urls import reverse

# Create your models here.

class TutorialThemeTheme(models.Model):
	name = models.CharField(max_length=50, primary_key=True, verbose_name='Тема тем обучалок')
	background = models.ImageField(upload_to='img/', verbose_name='Фон')

	def get_tutorialthemes_amount(self):
		return self.tutorialtheme_set.all().count()
	get_tutorialthemes_amount.short_description = 'Количество тем обучалок'
	def get_absolute_url(self):
		return reverse('tutorial-theme-theme-detail', args=[str(self.name)])
	def __str__(self):
		return self.name

class TutorialTheme(models.Model):
	name = models.CharField(max_length=50, primary_key=True, verbose_name='Тема обучалок')
	theme = models.ForeignKey('TutorialThemeTheme', on_delete=models.CASCADE, null=True, verbose_name='Тема темы')
	background = models.ImageField(upload_to='img/', verbose_name='Фон')

	def get_tutorials_amount(self):
		return self.tutorial_set.all().count()
	get_tutorials_amount.short_description = 'Количество обучалок'
	def get_absolute_url(self):
		return reverse('tutorial-theme', args=[str(self.theme), str(self.name)])
	def __str__(self):
		return self.name

class Tutorial(models.Model):
	name = models.CharField(max_length=50, verbose_name='Название обучалки', unique=True)
	theme = models.ForeignKey('TutorialTheme', on_delete=models.CASCADE, null=True, verbose_name='Тема')
	background = models.ImageField(upload_to='img/', verbose_name='Фон')
	def get_absolute_url(self):
		return f'/tutorials/{self.name}'
	def __str__(self):
		return self.name


class LevelThemeTheme(models.Model):
	name = models.CharField(max_length=50, primary_key=True, verbose_name='Тема тем уровней')
	background = models.ImageField(upload_to='img/', verbose_name='Фон')

	def get_levelthemes_amount(self):
		return self.leveltheme_set.all().count()
	get_levelthemes_amount.short_description = 'Количество тем уровней'
	def get_absolute_url(self):
		return reverse('level-theme-theme-detail', args=[str(self.name)])
	def __str__(self):
		return self.name

class LevelTheme(models.Model):
	name = models.CharField(max_length=50, verbose_name='Тема уровней', primary_key=True)
	theme = models.ForeignKey('LevelThemeTheme', on_delete=models.CASCADE, null=True, verbose_name='Тема')
	background = models.ImageField(upload_to='img/', verbose_name='Фон')
	
	def get_levels_amount(self):
		return self.level_set.all().count()
	get_levels_amount.short_description = 'Количество уровней'
	def get_absolute_url(self):
		return reverse('level-theme', args=[str(self.theme), str(self.name)])
	def __str__(self):
		return self.name

class Level(models.Model):
	name = models.CharField(max_length=50, verbose_name='Название уровня', unique=True)
	theme = models.ForeignKey('LevelTheme', on_delete=models.CASCADE, null=True, verbose_name='Тема')
	background = models.ImageField(upload_to='img/', verbose_name='Фон')
	def get_absolute_url(self):
		return f'/levels/{self.name}'
	def __str__(self):
		return self.name
	pass