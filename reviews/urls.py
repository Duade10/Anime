from django.urls import path
from . import views


app_name = "reviews"

urlpatterns = [
    path("submit/<int:movie_id>/", views.SubmitReview.as_view(), name="submit_review"),
]
