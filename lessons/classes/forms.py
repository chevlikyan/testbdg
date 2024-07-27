from django import forms

from .models import Class, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['type', 'title', 'description']


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['category', 'title', 'description', 'duration_in_months', 'slug']
