from django.shortcuts import render, redirect
from movies import models as movies_models
from django.views import View
from django.contrib import messages
from django.db.models import Q


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


class SearchException(Exception):
    pass


class Search(View):
    def get(self, request, *args, **kwargs):
        url = request.META.get("HTTP_REFERER")
        query = request.GET.get("query", None)
        try:
            if query is not None:
                movies = movies_models.Movie.objects.filter(
                    Q(title__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query)
                ).distinct()
                if movies.count() <= 0:
                    messages.error(request, "No result found")
                    raise SearchException()
                context = {"movies": movies, "query": query}
                return render(request, "core/search.html", context)
            messages.error(request, "You didn't fill the search form")
            raise SearchException()
        except SearchException:
            return redirect(url)
