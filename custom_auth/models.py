from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(
        max_length=12,
        verbose_name="Телефон",
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name='Активен',
        default=False
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.email