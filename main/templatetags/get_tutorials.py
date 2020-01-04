from django import template
from ..views import TutorialThemeTheme
register = template.Library()

@register.simple_tag
def get_tutorial_list(val=None):
	return TutorialThemeTheme.objects.all()

@register.simple_tag
def replacesymbols(val=None):
	output = val.replace('_', ' ')
	print(output)
	return output