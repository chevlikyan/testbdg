from django.contrib import admin
from .models import *


@admin.register(Category)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('type', 'description',)


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title',)
