from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("recently-added-movies/", views.RecentlyAddedMovies.as_view(), name="recent"),
    path("toggle-watchlist/<str:id>/", views.ToggleWatchlist.as_view(), name="toggle_watchlist"),
    path("add-to-watch/<str:id>/", views.AddToSession.as_view(), name="add_to_watch"),
    path("popular-movies/", views.PopularMovies.as_view(), name="popular"),
    path("detail/<str:slug>/", views.Detail.as_view(), name="detail"),
]
