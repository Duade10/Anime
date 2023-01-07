from django.urls import path
from . import views

app_name = "categories"

urlpatterns = [
    path("<str:slug>/", views.CategoryList.as_view(), name="movies"),
]
