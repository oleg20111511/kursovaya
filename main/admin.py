from django.contrib import admin

# Register your models here.
from .models import TutorialTheme, Tutorial, LevelThemeTheme, LevelTheme, Level


# @admin.register(TutorialThemeTheme)
# class TutorialThemeThemeAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'get_tutorialthemes_amount')

class TutorialInline(admin.TabularInline):
	model = Tutorial
	extra = 1

@admin.register(TutorialTheme)
class TutorialThemeAdmin(admin.ModelAdmin):
	list_display = ('name', 'get_tutorials_amount')
	inlines = [TutorialInline]

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
	search_fields = ('name', )
	list_display = ('name', 'theme')


@admin.register(LevelThemeTheme)
class LevelThemeThemeAdmin(admin.ModelAdmin):
	list_display = ('name', 'get_levelthemes_amount')

class LevelInline(admin.TabularInline):
	model = Level
	extra = 1

@admin.register(LevelTheme)
class LevelThemeAdmin(admin.ModelAdmin):
	list_display = ('name', 'get_levels_amount')
	inlines = [LevelInline]

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
	search_fields = ('name', )
	list_display = ('name', 'theme')