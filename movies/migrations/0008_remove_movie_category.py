# Generated by Django 4.1.5 on 2023-01-04 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0007_movie_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="category",
        ),
    ]
