# Generated by Django 3.2.16 on 2023-04-29 06:20

import custom_auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0002_auto_20230422_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_code',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Код активации'),
        ),
        migrations.AddField(
            model_name='user',
            name='activation_code_expires',
            field=models.DateTimeField(default=custom_auth.models.get_future),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email adress'),
        ),
    ]
