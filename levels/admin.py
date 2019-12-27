from django.contrib import admin

from .models import Level, Question, Answer
# Register your models here.

class QuestionInline(admin.TabularInline):
	exclude = ('use_template', 'customHTML')
	model = Question

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
	inlines = [QuestionInline]
	list_display = ('name', 'get_questions_amount')

class AnswerInline(admin.TabularInline):
	model = Answer
	extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('name', 'level')
	fieldsets = (
		(None, {
			'fields': ('name', 'level', 'customHTML', 'use_template')
		}),
		('Настройки шаблона', {
			'classes': ('collapse',),
			'fields': ('text', 'image', 'audio')
		})
	)
	inlines = [AnswerInline]