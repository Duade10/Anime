# Generated by Django 4.1.5 on 2023-01-04 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0003_remove_user_age_user_age_group"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("image", models.ImageField(upload_to="movies/images/")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Trailer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("file", models.FileField(null=True, upload_to="")),
                ("title", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                (
                    "age_limit",
                    models.CharField(
                        choices=[("all", "18 AND ABOVE"), ("child", "17 AND BELOW")],
                        max_length=15,
                    ),
                ),
                ("description", models.TextField()),
                ("banner", models.ImageField(upload_to="movies/banner/")),
                ("images", models.ManyToManyField(to="movies.image")),
                (
                    "trailer",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.trailer",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.admin",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
