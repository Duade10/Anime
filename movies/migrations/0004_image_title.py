# Generated by Django 4.1.5 on 2023-01-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_alter_movie_images"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
