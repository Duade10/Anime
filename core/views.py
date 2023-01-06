from django.shortcuts import render, redirect
from movies import models as movies_models
from django.views import View


class Index(View):
    def get(self, request, *args, **kwargs):
        movies = movies_models.Movie.objects.all()
        recently_added_movies = movies.order_by("-created")
        popular_movies = movies.order_by("-rating")
        context = {
            "recently_added_movies": recently_added_movies,
            "popular_movies": popular_movies,
            "movies": movies,
        }
        return render(request, "core/index.html", context)


class Watching(View):
    def get(self, request, *args, **kwargs):
        id = request.session.get("uuid")
        movie = movies_models.Movie.objects.get(id=id)
        context = {"movie": movie}
        return render(request, "core/watch.html", context)
