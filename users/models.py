from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator

# Account Verification Imports
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode


class User(AbstractUser):
    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_GMAIL = "gmail"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GMAIL, "gmail"),
        (LOGIN_GITHUB, "Github"),
    )

    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        NORMAL = "NORMAL", "Normal"

    type = models.CharField(max_length=50, choices=Types.choices, default=Types.NORMAL)
    phone_number = models.CharField(max_length=20, null=True)
    login_method = models.CharField(max_length=20, choices=LOGIN_CHOICES, null=True, blank=True)
    age = models.DateField()

    def save(self, *args, **kwargs):
        self.first_name = str.capitalize(self.first_name)
        self.last_name = str.capitalize(self.last_name)
        super().save(*args, **kwargs)

    def get_full_name(self) -> str:
        return super().get_full_name()

    def verify_email(self, request):
        current_site = get_current_site(request)
        domain = current_site
        uid = urlsafe_base64_encode(force_bytes(self.pk))
        token = default_token_generator.make_token(self)

        html_message = render_to_string(
            "users/mail/user_verification_email.html",
            {"domain": domain, "uidb64": uid, "token": token, "first_name": self.first_name},
        )
        send_mail(
            "Activate your Account",
            strip_tags(html_message),
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=False,
            html_message=html_message,
        )
        self.save()

    def send_reset_email(self, request):
        current_site = get_current_site(request)
        domain = current_site
        uid = urlsafe_base64_encode(force_bytes(self.pk))
        token = default_token_generator.make_token(self)

        html_message = render_to_string(
            "users/mail/reset_password_email.html",
            {"domain": domain, "uid": uid, "token": token, "first_name": self.first_name},
        )
        send_mail(
            "Reset Your Password",
            strip_tags(html_message),
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=False,
            html_message=html_message,
        )


class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)
        return queryset


class Admin(User):
    objects = AdminManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.ADMIN
        return super().save(*args, **kwargs)


class NormalUserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs).filter(type=User.Types.NORMAL)
        return queryset


class NormalUser(User):
    objects = NormalUserManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.NORMAL
        return super().save(*args, **kwargs)
