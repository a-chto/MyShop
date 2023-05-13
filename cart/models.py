from django.db import models
from django.contrib.sessions.models import Session
from django.core.validators import MinValueValidator


class Cart(models.Model):
    user = models.ForeignKey(
        to='custom_auth.User',
        verbous_name='Пользователь',
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        blank=True
    )
    session = models.ForeignKey(
        to=Session,
        verbous_name='Сессия',
        on_delete=models.CASCADE
    )

class CartItem(models.Model):
    product = models.ForeignKey(
        to='main.Product',
        verbose_name='Товар',
        on_delete=models.CASACDE
    )
    cart = models.ForeignKey(
        to=Cart,
        verbose_name='Корзина',
        on_delete=models.CASCADE,
        related_name='items'
    )
    count = models.PositiveSmallIntegerField(
        verbose_name='Количество в корзине',
        validators=[MinValueValidator(1)],
        default=1
    )
