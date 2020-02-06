from django import template
register = template.Library()

@register.simple_tag
def is_passed(level, user):
	user_scores = user.profile.scores_set.all()
	current_scores = user_scores.values('level')
	passed = False
	for i in current_scores:
		if level.id == i['level']:
			passed = True
			break
	return passed

@register.simple_tag
def get_range():
	return range(1, 6)

@register.simple_tag
def get_stars(level, user):
	user_scores = user.profile.scores_set.all()
	current_scores = user_scores.values('level')
	for i in current_scores:
		if level.id == i['level']: 
			score = user_scores.get(level=i['level'])
			stars = int(score.percents/20) + 1
			break
	return stars