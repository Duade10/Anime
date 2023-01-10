import random
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from . import models


class PopularMovies(ListView):
    model = models.Movie
    template_name = "movies/popular.html"
    context_object_name = "movies"
    page_kwarg = "page"
    paginate_by = 20
    paginate_orphans = 3

    def get_queryset(self):
        qs = super().get_queryset().order_by("-rating")
        return qs


class RecentlyAddedMovies(ListView):
    model = models.Movie
    template_name = "movies/recently_added.html"
    context_object_name = "movies"
    page_kwarg = "page"
    paginate_by = 20
    paginate_orphans = 3

    def get_queryset(self):
        qs = super().get_queryset().order_by("-created")
        return qs


class AddToSession(View):
    def get(self, request, id, *args, **kwargs):
        request.session["uuid"] = id
        return redirect(reverse("core:watching"))


class ToggleWatchlist(View):
    def get(self, request, id, *args, **kwargs):
        url = self.request.META.get("HTTP_REFERER")
        user = request.user
        movie = models.Movie.objects.get(id=id)
        if movie in user.watchlist.all():
            user.watchlist.remove(movie)
            messages.info(request, "Removed from watchlist")
        else:
            user.watchlist.add(movie)
            messages.success(request, "Added to watchlist")
        return redirect(url)


class Detail(View):
    def get(self, request, slug, *args, **kwargs):
        previous_url = request.META.get("HTTP_REFERER")
        try:
            movie = models.Movie.objects.get(slug=slug)
            category_list = []
            for category in movie.category.all():
                category_list.append(category.pk)
            category = random.sample(category_list, 1)
            category = int(str(category).replace("[", "").replace("]", ""))
            related_movies = models.Movie.objects.filter(category__pk=category).exclude(pk=movie.pk)
            if len(related_movies) >= 4:
                related_movies = random.sample(list(related_movies), 4)
        except models.Movie.DoesNotExist:
            if previous_url:
                return redirect(previous_url)
            return redirect("core:index")
        context = {"movie": movie, "related_movies": related_movies}
        return render(request, "movies/detail.html", context)
