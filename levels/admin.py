from django.contrib import admin

from .models import Level, Question, Answer
# Register your models here.

class QuestionInline(admin.TabularInline):
	exclude = ('use_template', 'customHTML')
	model = Question

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
	view_on_site = True
	inlines = [QuestionInline]
	list_display = ('name', 'get_questions_amount')

class AnswerInline(admin.TabularInline):
	model = Answer
	extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	search_fields = ('name', )
	list_display = ('name', 'level')
	fieldsets = (
		(None, {
			'fields': ('name', 'level', 'customHTML', 'use_template', 'qtype')
		}),
		('Настройки шаблона', {
			'classes': ('collapse',),
			'fields': ('text', 'image', 'audio')
		})
	)
	inlines = [AnswerInline]