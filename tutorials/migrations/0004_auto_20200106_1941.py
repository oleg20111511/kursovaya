# Generated by Django 2.2.7 on 2020-01-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_auto_20200106_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название правила'),
        ),
    ]
