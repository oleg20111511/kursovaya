from django.shortcuts import render
from .models import Level
from main.models import Level as ProfileLevel
from profiles.models import Scores
from django.views import generic
from django.http import JsonResponse
# Create your views here.

class LevelDetailView(generic.DetailView):
	model = Level

def SaveScoreView(request, pk):
	result = int(float(request.POST.get('result')))
	user = request.user
	user_scores = user.profile.scores_set.all()
	current_scores = user_scores.values('level')
	passed = False
	for i in current_scores:
		level = ProfileLevel.objects.get(pk=i['level'])
		if level.name == pk:
			passed = True
			break
	if passed:
		score = user_scores.get(level=i['level'])
		if score.percents < result:
			score.percents = result
			score.save()
	else:
		Scores.objects.create(percents=result, profile=user.profile, level=ProfileLevel.objects.get(name=pk))

	request.session['LastLevel'] = pk
	request.session['Result'] = result
	print(f'save {result}, {pk}')
	return JsonResponse({'success': True})

def LevelFinish(request, pk):
	levelname = request.session.get('LastLevel', None)
	percents = request.session.get('Result', None)
	if (levelname != pk) or (percents==None):
		return render(request, 'error.html')
	else:
		level = ProfileLevel.objects.get(name=pk)
		stars = int(percents / 20) + 1
		context = {'level': level, 'stars': stars, 'range': range(1, 6), 'finished': True}
		return render(request, 'finish_level.html', context)