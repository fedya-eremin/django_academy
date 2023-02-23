from catalog.validators import GreatValidator

from core.models import AbstractCatalog, AbstractWithSlug, NormalizedField

import django.core.validators
import django.db.models


class Tag(AbstractCatalog, AbstractWithSlug, NormalizedField):
    """
    model which describes tag.
    has AbstractCatalog's inner fields and slug
    """

    class Meta:
        verbose_name = "тэг"
        verbose_name_plural = "тэги"


class Category(AbstractCatalog, AbstractWithSlug, NormalizedField):
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
            django.core.validators.MinValueValidator(1),
            django.core.validators.MaxValueValidator(32767),
        ],
        help_text="Вес - число от 0 до 32767",
    )


class Item(AbstractCatalog, NormalizedField):
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
