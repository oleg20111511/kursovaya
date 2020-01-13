from django import template
from ..views import TutorialTheme
register = template.Library()

@register.simple_tag
def get_tutorial_list(val=None):
	return TutorialTheme.objects.all()

@register.simple_tag
def replacesymbols(val=None):
	output = val.replace('_', ' ')
	return output