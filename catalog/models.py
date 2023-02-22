from catalog.validators import GreatValidator

import core.models

import django.core.exceptions
import django.core.validators
import django.db.models


class Tag(core.models.AbstractCatalog):
    """
    model which describes tag.
    has AbstractCatalog's inner fields and slug
    """

    class Meta:
        verbose_name = "тэг"
        verbose_name_plural = "тэги"

    slug = django.db.models.SlugField(
        "Слизняк",
        unique=True,
        max_length=200,
        help_text="Впишите slug-последовательность в поле",
    )


class Category(core.models.AbstractCatalog):
    """
    model which describes category.
    has AbstractCatalog's inner fields and slug & weight
    """

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    weight = django.db.models.IntegerField(
        "Вес",
        default=100,
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(32767),
        ],
        help_text="Вес - число от 0 до 32767",
    )
    slug = django.db.models.SlugField(
        "Слизняк",
        unique=True,
        max_length=200,
        help_text="Впишите slug-последовательность в поле",
    )


class Item(core.models.AbstractCatalog):
    """
    model which describes item.
    has AbstractCatalog's inner fields, text,
    category(one-to-many), tags(many-to-many)
    """

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    text = django.db.models.TextField(
        "Описание",
        validators=[
            GreatValidator("превосходно", "роскошно"),
        ],
        help_text='Текст должен содержать слово "превосходно" или "роскошно"',
    )
    category = django.db.models.ForeignKey(
        Category, on_delete=django.db.models.CASCADE, default=None
    )
    tags = django.db.models.ManyToManyField(Tag)
