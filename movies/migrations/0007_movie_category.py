# Generated by Django 4.1.5 on 2023-01-04 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
        ("movies", "0006_remove_movie_images_image_movie"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="categories.category",
            ),
        ),
    ]
