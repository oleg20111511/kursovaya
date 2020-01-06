# Generated by Django 2.2.7 on 2019-12-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0002_question_qtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qtype',
            field=models.IntegerField(choices=[(0, 'Один вариант ответа'), (1, 'Несколько вариантов ответа'), (2, 'Ввод ответа')], default='0', help_text='Какие будут ответы на вопрос', verbose_name='Тип вопроса'),
        ),
    ]