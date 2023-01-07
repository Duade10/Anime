from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("<str:slug>/", views.Detail.as_view(), name="detail"),
    path("add-to-watch/<str:id>/", views.AddToSession.as_view(), name="add_to_watch"),
    path("recently-added-movies/", views.RecentlyAddedMovies.as_view(), name="recent"),
    path("toggle-watchlist/<str:id>/", views.ToggleWatchlist.as_view(), name="toggle_watchlist"),
]
