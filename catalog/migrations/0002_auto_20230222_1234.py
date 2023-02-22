# Generated by Django 3.2.16 on 2023-02-22 12:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="slug",
        ),
        migrations.AlterField(
            model_name="category",
            name="is_published",
            field=models.BooleanField(
                default=True, verbose_name="Опубликовано"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.TextField(
                help_text="Имя, содержит до 150 символов",
                max_length=150,
                verbose_name="Имя",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="weight",
            field=models.IntegerField(
                default=100,
                help_text="Вес - число от 0 до 32767",
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(32767),
                ],
                verbose_name="Вес",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="is_published",
            field=models.BooleanField(
                default=True, verbose_name="Опубликовано"
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.TextField(
                help_text="Имя, содержит до 150 символов",
                max_length=150,
                verbose_name="Имя",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="is_published",
            field=models.BooleanField(
                default=True, verbose_name="Опубликовано"
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.TextField(
                help_text="Имя, содержит до 150 символов",
                max_length=150,
                verbose_name="Имя",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(
                help_text="Впишите slug-последовательность в поле",
                max_length=200,
                unique=True,
                verbose_name="Слизняк",
            ),
        ),
    ]
