from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    type = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=30, null=True, blank=True, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.type


class Class(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    duration_in_months = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
