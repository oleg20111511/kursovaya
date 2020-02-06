from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from main.models import Level


class MyRegisterFormView(FormView):
	form_class = UserCreationForm
	success_url = "/accounts/login/"
	template_name = "register.html"

	def form_valid(self, form):
		form.save()
		return super(MyRegisterFormView, self).form_valid(form)

	def form_invalid(self, form):
		return super(MyRegisterFormView, self).form_invalid(form)

def ProfilePage(request, pk):
	if request.user.id != int(pk):
		return render(request, 'profile_error.html')
	else:
		context = {}
		user = request.user
		scores = user.profile.scores_set.all()
		result = 0
		total = 0
		for score in scores:
			result += score.percents
			total += 1
		result = int(result / total)
		context['result'] = result
		context['total'] = total
		context['levels'] = Level.objects.all().count()
		return render(request, 'ProfilePage.html', context)