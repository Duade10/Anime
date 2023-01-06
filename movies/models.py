from django.db import models
from django.urls import reverse
from core.models import AbstractTimeStampModel
from users import models as users_models
from django.utils.text import slugify
from reviews.models import Review
from django.db.models.aggregates import Avg, Count


class Movie(AbstractTimeStampModel):
    class Types(models.TextChoices):
        MOVIE = "MOVIE", "movie"
        SERIES = "SERIES", "series"

    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    age_limit = models.CharField(choices=users_models.User.AGE_GROUP_CHOICES, max_length=15)
    description = models.TextField()
    banner = models.ImageField(upload_to="movies/banner/")
    user = models.ForeignKey("users.Admin", related_name="movies", on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField("categories.Category", related_name="movies")
    rating = models.FloatField(null=True, blank=True)
    type = models.CharField(choices=Types.choices, max_length=10, null=True, blank=True)
    date_aired = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def averageRating(self):
        reviews = Review.objects.filter(movie=self, status=True).aggregate(average=Avg("rating"))
        avg = 0
        if reviews["average"] is not None:
            avg = float(reviews["average"])
        return avg

    def countReview(self):
        reviews = Review.objects.filter(movie=self, status=True).aggregate(count=Count("review"))
        count = 0
        if reviews["count"] is not None:
            count = int(reviews["count"])
        return count

    def get_absolute_url(self):
        return reverse("movies:detail", kwargs={"slug": self.slug})

    def get_add_to_watch_url(self):
        return reverse("movies:add_to_watch", kwargs={"id": self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)  # Call the real save() method


class Trailer(AbstractTimeStampModel):
    file = models.FileField(null=True)
    title = models.CharField(max_length=255)
    movie = models.OneToOneField(Movie, related_name="trailer", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Image(AbstractTimeStampModel):
    image = models.ImageField(upload_to="movies/images/")
    title = models.CharField(max_length=255, unique=True, blank=True, null=True)
    movie = models.ForeignKey(Movie, related_name="images", on_delete=models.CASCADE, null=True, blank=True)
