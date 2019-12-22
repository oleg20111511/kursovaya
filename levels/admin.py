from django.contrib import admin

from .models import Level, Question, Answer
# Register your models here.

class QuestionInline(admin.TabularInline):
	model = Question

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
	inlines = [QuestionInline]
	pass

class AnswerInline(admin.TabularInline):
	model = Answer
	extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInline]
	pass