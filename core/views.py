from django.shortcuts import render, redirect
from movies import models as movies_models
from django.views import View


class Index(View):
    def get(self, request, *args, **kwargs):
        movies = movies_models.Movie.objects.all()
        recently_added_movies = movies.order_by("-created")[:6]
        popular_movies = movies.order_by("-rating")[:6]
        watchlist_movies = request.user.watchlist.all()[:6]
        context = {
            "recently_added_movies": recently_added_movies,
            "popular_movies": popular_movies,
            "watchlist_movies": watchlist_movies,
            "movies": movies,
        }
        return render(request, "core/index.html", context)


class Watching(View):
    def get(self, request, *args, **kwargs):
        id = request.session.get("uuid")
        movie = movies_models.Movie.objects.get(id=id)
        context = {"movie": movie}
        return render(request, "core/watch.html", context)
