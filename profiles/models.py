from django.db import models
from main.models import Level
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

class Scores(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Пользователь')
	percents = models.IntegerField(verbose_name='Результат')
	level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='Уровень')
	def __str__(self):
		return self.level.name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()