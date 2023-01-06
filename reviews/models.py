from django.db import models
from core.models import AbstractTimeStampModel


class Review(AbstractTimeStampModel):
    movie = models.ForeignKey("movies.Movie", related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)

    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"{self.subject} - {self.full_name()}"
