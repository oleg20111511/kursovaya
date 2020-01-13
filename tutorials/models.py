from django.db import models
from django.urls import reverse

# Create your models here.

class Tutorial(models.Model):
	name = models.CharField(max_length=100, verbose_name='Название обучалки', primary_key=True)
	theme = models.CharField(max_length=50, verbose_name='Тема обучалки', help_text='Отображается вверху страницы')
	def get_rules_amount(self):
		return self.rule_set.all().count()
	get_rules_amount.short_description = 'Количество правил'
	def __str__(self):
		return self.name

class Rule(models.Model):
	name = models.CharField(max_length=100, verbose_name='Название правила')
	tutorial = models.ForeignKey(Tutorial, on_delete=models.SET_NULL, verbose_name='Обучалка', null=True)
	use_template = models.BooleanField(default=True, verbose_name='Использовать шаблон?')
	image = models.ImageField(upload_to='tutorials/img/', null=True, verbose_name='Картинка', blank=True)
	text = models.CharField(max_length=500, null=True, verbose_name='Надпись', blank=True)
	audio = models.FileField(upload_to='tutorials/audio/', null=True, verbose_name='Аудио', blank=True)
	customHTML = models.FileField(upload_to='tutorials/customHTML/', null=True, verbose_name='Свой вариант страницы', blank=True, help_text='Не работает, если включено "Использовать шаблон"')
	def __str__(self):
		return self.name