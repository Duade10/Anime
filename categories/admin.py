from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created", "updated", "movies_count"]

    def movies_count(self, obj):
        return obj.movies.count()

    movies_count.short_description = "movies"
