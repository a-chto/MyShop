from django.db import models

from django.core.validators import MaxValueValidator

from . import mixins

from pytils.translit import slugify


def upload_to(instance, filename:str) -> str:
    '''
    получаем путь для загрузки изображения
    instance: объект Category или ProductImage
    filename: имя загружаемого файла
    '''
    if  isinstance(instance, Category):
        return '/'.join(['categories', instance.name, filename])
    if isinstance(instance, ProductImage):
        return '/'.join(['products', product.category.name, product.name, filename])


class Category(mixins.ActiveMixin):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Название категории'
    )
    image = models.ImageField (
        upload_to='category',
        null=True,
        verbose_name='Изображение категории'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def _str__(self) -> str:
        return self.name


class Product(mixins.ActiveMixin):
    slug = models.SlugField(
        verbose_name='Слаг',
        default='',
        max_length=50,
        unique=True
    )
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Название категории'
        )
    category = models.ForeignKey(
        to=Category,
        verbose_name='Категория товара',
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True
    )
    price = models.DecimalField(
        verbose_name='Цена товара',
        max_digits=9,
        decimal_places=2,
        default=0
    )
    discount_percent = models.PositiveSmallIntegerField(
        verbose_name='Скидка в процентах',
        null=True,
        default=None,
        validators=[MaxValueValidator(100)]
    )
    count = models.PositiveIntegerField(
        verbose_name='Остаток',
        default=0,
        blank=False
    )

    class Meta: #запрещена в рф
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.pk}{self.name}')[:50]
        super().save(*args, **kwargs)

    @property
    def price_with_discount(self):
        if self.discount_percent > 0:
            return self.price - (self.price * self.discount_percent / 100)
        return self.price



class ProductImage(models.Model):
    image = models.ImageField(
        upload_to='product',
        null=True,
        verbose_name='Изображение товара'
    )
    product = models.ForeignKey(
        to=Product,
        verbose_name='Товар',
        null=True,
        on_delete=models.CASCADE
    )