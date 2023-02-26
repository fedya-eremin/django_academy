from pathlib import Path

from django.conf import settings
import django.core.validators
import django.db.models
import django.utils.safestring
from sorl.thumbnail import get_thumbnail

from catalog.validators import GreatValidator
from core.models import AbstractCatalog, AbstractWithSlug, NormalizedField


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
    main_image = django.db.models.ImageField(
        upload_to="titles",
        default="../static_dev/img/cat-logo.png",
        blank=True,
        null=True,
    )

    def get_image_300x300(self):
        return get_thumbnail(
            self.main_image, "300x300", crop="center", quality=51
        )

    def image_thumbnail(self):
        if self.main_image:
            return django.utils.safestring.mark_safe(
                    f'<img src="{self.main_image.url}" height=50>'
            )

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "превью"

    list_display = "image_thumbnail",


class Gallery(django.db.models.Model):
    """
    model which stores all additional item images
    """

    class Meta:
        verbose_name = "допольнительное фото"
        verbose_name_plural = "допольнительные фото"

    item = django.db.models.ForeignKey(
        Item, on_delete=django.db.models.CASCADE, default=None
    )
    image = django.db.models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.image.url
