from django.contrib import admin

from .models import Tutorial, Rule
# Register your models here.

class RuleInline(admin.TabularInline):
	exclude = ('use_template', 'customHTML')
	model = Rule

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
	view_on_site = True
	inlines = [RuleInline]
	list_display = ('name', 'get_rules_amount')

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
	search_fields = ('name', )
	list_display = ('name', 'tutorial')
	fieldsets = (
		(None, {
			'fields': ('name', 'tutorial', 'customHTML', 'use_template')
		}),
		('Настройки шаблона', {
			'classes': ('collapse',),
			'fields': ('text', 'image', 'audio')
		})
	)