from django.contrib import admin
from . import models


class ImageInline(admin.TabularInline):
    model = models.Image


class TrailerInline(admin.TabularInline):
    model = models.Trailer


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "age_limit", "rating", "created", "updated"]
    search_fields = ["title__icontains", "age_limit", "user__username", "category__name__icontains"]
    inlines = (TrailerInline, ImageInline)
