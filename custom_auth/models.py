from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(
        max_length=12,
        verbose_name="Телефон",
        null=True,
        blank=True
    )