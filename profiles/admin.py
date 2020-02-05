from django.contrib import admin
from .models import Profile, Scores
# Register your models here.

class ScoresInline(admin.TabularInline):
	model = Scores
	extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	inlines = [ScoresInline]
	pass

@admin.register(Scores)
class ScoresAdmin(admin.ModelAdmin):
	pass