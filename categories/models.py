from django.db import models
from core.models import AbstractTimeStampModel
from django.utils.text import slugify


class Category(AbstractTimeStampModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
