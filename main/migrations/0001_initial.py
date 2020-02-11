# Generated by Django 2.2.7 on 2020-01-03 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LevelTheme',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Тема уровней:')),
                ('background', models.ImageField(upload_to='img/', verbose_name='Фон:')),
            ],
        ),
        migrations.CreateModel(
            name='TutorialThemeTheme',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Тема обучалок:')),
                ('background', models.ImageField(upload_to='img/', verbose_name='Фон:')),
            ],
        ),
        migrations.CreateModel(
            name='TutorialTheme',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Тема обучалок:')),
                ('background', models.ImageField(upload_to='img/', verbose_name='Фон:')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.TutorialThemeTheme', verbose_name='Тема темы:')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название обучалки:')),
                ('background', models.ImageField(upload_to='img/', verbose_name='Фон:')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.TutorialTheme', verbose_name='Тема:')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название уровня')),
                ('background', models.ImageField(upload_to='img/', verbose_name='Фон:')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.LevelTheme', verbose_name='Тема:')),
            ],
        ),
    ]