from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator

from . import models


class CategoryMovies(View):
    def get(self, request, slug, *args, **kwargs):
        category = models.Category.objects.get(slug=slug)
        movies = category.movies.all()
        paginator = Paginator(movies, 20)
        page_number = request.GET.get("page")
        movies = paginator.get_page(page_number)
        context = {"movies": movies, "category": category}
        return render(request, "categories/movies.html", context)


class CategoryList(ListView):
    model = models.Category
    template_name = "categories/list.html"
    context_object_name = "categories"
    paginate_by = 2
    paginate_orphans = 3
    page_kwarg = "page"
