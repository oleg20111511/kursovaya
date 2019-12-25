from django import template
from django.core.files import File
register = template.Library()

# Да, костыль. Нет, не стыдно
@register.simple_tag
def sort_answers(answers=None):
	right_answers = []
	wrong_answers = []
	for i in answers:
		if i.correct:
			right_answers.append(i.value)
		else:
			wrong_answers.append(i.value)
	answers_dict = {'right': right_answers, 'wrong': wrong_answers}
	return answers_dict

@register.simple_tag
def tostring(file=None):
	with open(file, 'r') as f:
		doc = File(f)
		output = doc.read()

	return output