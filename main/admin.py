from django.contrib import admin

# Register your models here.
from .models import TutorialTheme, Tutorial, LevelTheme, Level

class TutorialInline(admin.TabularInline):
	model = Tutorial
	extra = 1

@admin.register(TutorialTheme)
class TutorialThemeAdmin(admin.ModelAdmin):
	list_display = ('name', 'get_tutorials_amount')
	inlines = [TutorialInline]

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
	list_display = ('name', 'theme')



class LevelInline(admin.TabularInline):
	model = Level
	extra = 1

@admin.register(LevelTheme)
class LevelThemeAdmin(admin.ModelAdmin):
	list_display = ('name', 'get_levels_amount')
	inlines = [LevelInline]

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
	list_display = ('name', 'theme')