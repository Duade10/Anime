# Generated by Django 4.1.5 on 2023-01-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0013_movie_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
