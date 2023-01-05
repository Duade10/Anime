from django.contrib import admin
from . import models


class ImageInline(admin.TabularInline):
    model = models.Image


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "age_limit", "rating", "created", "updated", "category"]
    search_fields = ["title__icontains", "age_limit", "user__username", "category__name__icontains"]
    inlines = (ImageInline,)


@admin.register(models.Trailer)
class TrailerAdmin(admin.ModelAdmin):
    pass
