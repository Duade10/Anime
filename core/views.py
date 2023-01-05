from django.shortcuts import render
from movies import models as movies_models


def index(request):
    movies = movies_models.Movie.objects.all()
    recently_added_movies = movies.order_by("-created")
    popular_movies = movies.order_by("-rating")
    context = {
        "recently_added_movies": recently_added_movies,
        "popular_movies": popular_movies,
        "movies": movies,
    }
    return render(request, "core/index.html", context)
