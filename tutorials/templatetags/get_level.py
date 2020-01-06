from django import template
from main.models import Level
register = template.Library()

@register.simple_tag
def get_level_image(name=None):
	level = Level.objects.get(name=name)
	image = level.background.url
	return image