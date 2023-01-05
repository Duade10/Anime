from django.db import models
from core.models import AbstractTimeStampModel
from users import models as users_models


class Movie(AbstractTimeStampModel):
    title = models.CharField(max_length=255)
    age_limit = models.CharField(choices=users_models.User.AGE_GROUP_CHOICES, max_length=15)
    description = models.TextField()
    banner = models.ImageField(upload_to="movies/banner/")
    trailer = models.OneToOneField(
        "movies.Trailer", related_name="movies", blank=True, null=True, on_delete=models.CASCADE
    )
    user = models.ForeignKey("users.Admin", related_name="movies", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey("categories.Category", related_name="movies", on_delete=models.SET_DEFAULT, default=1)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class Trailer(AbstractTimeStampModel):
    file = models.FileField(null=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Image(AbstractTimeStampModel):
    image = models.ImageField(upload_to="movies/images/")
    title = models.CharField(max_length=255, unique=True, blank=True, null=True)
    movie = models.ForeignKey(Movie, related_name="images", on_delete=models.CASCADE, null=True, blank=True)
