from django.contrib import admin

# Register your models here.
from .models import TutorialTheme, Tutorial, LevelTheme, Level

# admin.site.register(TutorialTheme)
# admin.site.register(Tutorial)
# admin.site.register(LevelTheme)
# admin.site.register(Level)

class TutorialInline(admin.TabularInline):
	model = Tutorial
	extra = 1

@admin.register(TutorialTheme)
class TutorialThemeAdmin(admin.ModelAdmin):
	inlines = [TutorialInline]
	pass

@admin.register(Tutorial)
class TutorialTdmin(admin.ModelAdmin):
	pass



class LevelInline(admin.TabularInline):
	model = Level
	extra = 1

@admin.register(LevelTheme)
class LevelThemeAdmin(admin.ModelAdmin):
	inlines = [LevelInline]
	pass

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
	pass