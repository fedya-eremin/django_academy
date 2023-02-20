from core.models import AbstractCatalog

import django.core.exceptions
import django.core.validators
import django.db.models


def great_validator(value):
    if "превосходно" not in value and "роскошно" not in value:
        raise django.core.exceptions.ValidationError(
            "Поле должно содержать 'превосходно' или 'роскошно'!"
        )


class CatalogTag(AbstractCatalog):
    """
    model which describes tag.
    has AbstractCatalog's inner fields and slug
    """

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    slug = django.db.models.TextField(
        "Слизняк",
        unique=True,
        validators=[django.core.validators.validate_slug],
        max_length=200,
    )

    def __str__(self):
        return self.name


class CatalogCategory(AbstractCatalog):
    """
    model which describes category.
    has AbstractCatalog's inner fields and slug & weight
    """

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    slug = django.db.models.TextField(
        "Слизняк",
        unique=True,
        validators=[django.core.validators.validate_slug],
        max_length=200,
        help_text="Выберите категорию из списка",
    )
    weight = django.db.models.IntegerField(
        "Вес",
        default=100,
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(32767),
        ],
        help_text="Вес - число от 0 до 32767",
    )

    def __str__(self):
        return self.name


class CatalogItem(AbstractCatalog):
    """
    model which describes item.
    has AbstractCatalog's inner fields, text,
    category(one-to-many), tags(many-to-many)
    """

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    text = django.db.models.TextField(
        "Описание",
        validators=[
            great_validator,
        ],
        help_text='Текст должен содержать слово "превосходно" или "роскошно"',
    )
    category = django.db.models.ForeignKey(
        CatalogCategory, on_delete=django.db.models.CASCADE,
        default=None
    )
    tags = django.db.models.ManyToManyField(CatalogTag)

    def __str__(self):
        return self.name
