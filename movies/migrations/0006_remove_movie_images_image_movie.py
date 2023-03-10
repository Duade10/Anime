# Generated by Django 4.1.5 on 2023-01-04 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0005_remove_movie_poster"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="images",
        ),
        migrations.AddField(
            model_name="image",
            name="movie",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="movies.movie",
            ),
        ),
    ]
