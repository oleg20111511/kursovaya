from django.db import models
from django.urls import reverse

# Create your models here.

class Level(models.Model):
	name = models.CharField(max_length=100, verbose_name='Название уровня:', primary_key=True)
	def get_absolute_url(self):
		return reverse('level', args=[str(self.name)])
	def __str__(self):
		return self.name

class Question(models.Model):
	name = models.CharField(max_length=100, verbose_name='Название вопроса:')
	level = models.ForeignKey(Level, on_delete=models.SET_NULL, verbose_name='Уровень:', null=True)
	use_template = models.BooleanField(default=True, verbose_name='Использовать шаблон?')
	image = models.ImageField(upload_to='levels/img/', null=True, verbose_name='Картинка:', blank=True)
	text = models.CharField(max_length=500, null=True, verbose_name='Надпись:', blank=True)
	audio = models.FileField(upload_to='levels/audio/', null=True, verbose_name='Аудио:', blank=True)
	customHTML = models.FileField(upload_to='levels/customHTML', null=True, verbose_name='Свой вариант страницы:', blank=True)
	QUESTION_TYPE = (
		(0, 'Один вариант ответа'),
		(1, 'Несколько вариантов ответа'),
		(2, 'Ввод ответа'),
	)
	qtype = models.IntegerField(choices=QUESTION_TYPE, default='0', verbose_name='Тип вопроса', help_text='Какие будут ответы на вопрос')
	def __str__(self):
		return self.name

class Answer(models.Model):
	value = models.CharField(max_length=100, verbose_name='Ответ: ')
	correct = models.BooleanField(default=False, verbose_name='Правильный:')
	question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, verbose_name='Вопрос:')
	def __str__(self):
		return self.value