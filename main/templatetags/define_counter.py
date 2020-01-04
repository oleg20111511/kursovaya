from django import template
register = template.Library()

@register.simple_tag
def define(val=None):
	return val

@register.simple_tag
def decideCB(val=None):
	if (val - 1) % 4 == 0:
		return True
	else:
		return False

@register.simple_tag
def increase(val=None):
	val += 1
	return val