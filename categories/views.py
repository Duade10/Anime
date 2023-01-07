from django.shortcuts import render
from django.views import View
from . import models


class CategoryList(View):
    def get(self, request, slug, *args, **kwargs):
        category = models.Category.objects.get(slug=slug)
        movies = category.movies.all()
        context = {"movies": movies, "category": category}
        return render(request, "categories/movies.html", context)
