# Generated by Django 2.2.7 on 2019-12-14 17:34

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
                ('name', models.CharField(help_text='Тема уровней', max_length=50, primary_key=True, serialize=False)),
                ('background', models.CharField(default='img/working.jpg', help_text='Ссылка/путь к картинке для фона', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TutorialTheme',
            fields=[
                ('name', models.CharField(help_text='Тема обучалок', max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название обучалки', max_length=50)),
                ('background', models.CharField(default='img/working.jpg', help_text='Ссылка/путь к картинке для фона', max_length=500)),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.TutorialTheme')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название уровня', max_length=50)),
                ('background', models.CharField(default='img/working.jpg', help_text='Ссылка/путь к картинке для фона', max_length=500)),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.LevelTheme')),
            ],
        ),
    ]
