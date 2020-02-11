# Generated by Django 2.2.7 on 2020-01-03 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='background',
            field=models.ImageField(upload_to='img/', verbose_name='Фон'),
        ),
        migrations.AlterField(
            model_name='level',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.LevelTheme', verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='leveltheme',
            name='background',
            field=models.ImageField(upload_to='img/', verbose_name='Фон'),
        ),
        migrations.AlterField(
            model_name='leveltheme',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Тема уровней'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='background',
            field=models.ImageField(upload_to='img/', verbose_name='Фон'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.TutorialTheme', verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='tutorialtheme',
            name='background',
            field=models.ImageField(upload_to='img/', verbose_name='Фон'),
        ),
        migrations.AlterField(
            model_name='tutorialtheme',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Тема обучалок'),
        ),
        migrations.AlterField(
            model_name='tutorialtheme',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.TutorialThemeTheme', verbose_name='Тема темы'),
        ),
        migrations.AlterField(
            model_name='tutorialthemetheme',
            name='background',
            field=models.ImageField(upload_to='img/', verbose_name='Фон'),
        ),
        migrations.AlterField(
            model_name='tutorialthemetheme',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Тема тем обучалок'),
        ),
    ]