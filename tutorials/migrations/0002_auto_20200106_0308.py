# Generated by Django 2.2.7 on 2020-01-06 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='tutorials/audio/', verbose_name='Аудио'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='customHTML',
            field=models.FileField(blank=True, help_text='Не работает, если включено "Использовать шаблон"', null=True, upload_to='tutorials/customHTML', verbose_name='Свой вариант страницы'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tutorials/img/', verbose_name='Картинка'),
        ),
    ]
