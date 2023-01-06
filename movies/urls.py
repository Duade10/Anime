from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("<str:slug>/", views.Detail.as_view(), name="detail"),
    path("add-to-watch/<str:id>/", views.AddToSession.as_view(), name="add_to_watch"),
]
