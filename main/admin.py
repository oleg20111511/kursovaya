from django.contrib import admin

# Register your models here.
from .models import TutorialTheme, Tutorial, LevelTheme, Level

class TutorialInline(admin.TabularInline):
	model = Tutorial
	extra = 1

@admin.register(TutorialTheme)
class TutorialThemeAdmin(admin.ModelAdmin):
	inlines = [TutorialInline]

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
	pass



class LevelInline(admin.TabularInline):
	model = Level
	extra = 1

@admin.register(LevelTheme)
class LevelThemeAdmin(admin.ModelAdmin):
	inlines = [LevelInline]

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
	pass