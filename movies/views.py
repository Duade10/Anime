from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from . import models

# Create your views here.
class Detail(View):
    def get(self, request, slug, *args, **kwargs):
        previous_url = request.META.get("HTTP_REFERER")
        try:
            movie = models.Movie.objects.get(slug=slug)
        except models.Movie.DoesNotExist:
            if previous_url:
                return redirect(previous_url)
            return redirect("core:index")
        context = {"movie": movie}
        return render(request, "movies/detail.html", context)


class AddToSession(View):
    def get(self, request, id, *args, **kwargs):
        request.session["uuid"] = id
        print(request.session.get("uuid"))
        return redirect(reverse("core:watching"))
