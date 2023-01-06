from django.shortcuts import redirect
from django.views import View
from . import models, forms
from django.contrib import messages
from movies.models import Movie


class SubmitReview(View):
    def post(self, request, movie_id, *args, **kwargs):
        url = request.META.get("HTTP_REFERER")
        movie = Movie.objects.get(id=movie_id)
        if request.method == "POST":
            try:
                review = models.Review.objects.get(user__id=request.user.id, movie=movie)
                form = forms.ReviewForm(request.POST, instance=review)
                form.save()
                messages.success(request, "Thank you. Your review has been updated.")
                return redirect(url)
            except models.Review.DoesNotExist:
                form = forms.ReviewForm(request.POST)
                if form.is_valid():
                    data = models.Review()
                    data.subject = form.cleaned_data["subject"]
                    data.rating = form.cleaned_data["rating"]
                    data.review = form.cleaned_data["review"]
                    data.ip = request.META.get("REMOTE_ADDR")
                    data.movie = movie
                    data.user = self.request.user
                    data.save()
                    messages.success(request, "Thank you. Your review has been submitted.")
                    return redirect(url)
