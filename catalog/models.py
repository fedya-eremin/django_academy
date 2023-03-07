from catalog.validators import GreatValidator

from core.models import (
    AbstractCatalog,
    AbstractImage,
    AbstractWithSlug,
    NormalizedField,
)

import django.core.validators
import django.db.models
import django.utils.safestring
from django.shortcuts import get_object_or_404

from django_quill.fields import QuillField


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


class ItemManager(django.db.models.Manager):
    """
    a simple query manager for Item. I think its functionality is clear
    """

    def base_query(self):
        return (
            self.get_queryset()
            .select_related("category")
            .order_by("category__name")
            .prefetch_related(
                django.db.models.Prefetch(
                    "tags",
                    queryset=Tag.objects.filter(is_published=True).only(
                        "name"
                    ),
                )
            )
            .only("name", "text", "category__name")
            .filter(category__is_published=True, is_published=True)
        )

    def mainpage(self):
        return self.base_query().filter(is_on_main=True)

    def get_clearly(self, key):
        return get_object_or_404(
            self.get_queryset()
            .prefetch_related(
                django.db.models.Prefetch(
                    "gallery", queryset=Gallery.objects.filter(item=key)
                ),
            )
            .only("name", "text", "image"),
            pk=key,
        )


class Item(AbstractCatalog, NormalizedField, AbstractImage):
    """
    model which describes item.
    has AbstractCatalog's inner fields, text,
    category(one-to-many), tags(many-to-many)
    """

    objects = ItemManager()

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ("name",)

    text = QuillField(
        "Описание",
        validators=[
            GreatValidator("превосходно", "роскошно"),
        ],
        help_text='Текст должен содержать слово "превосходно" или "роскошно"',
    )

    is_on_main = django.db.models.BooleanField("На главной", default=False)
    category = django.db.models.ForeignKey(
        Category,
        on_delete=django.db.models.CASCADE,
        default=None,
        verbose_name="категория",
    )
    tags = django.db.models.ManyToManyField(Tag, verbose_name="тэги")

    def image_thumbnail(self):
        """shows item's thumbnail on the dashboard of table"""
        if self.image:
            return django.utils.safestring.mark_safe(
                f'<img src="{self.get_thumb_50x50.url}" />'
            )
        return "no title image"

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "превью"


class TitleImage(django.db.models.Model):
    class Meta:
        verbose_name = "иконка"
        verbose_name_plural = "иконки"

    item = django.db.models.OneToOneField(
        Item,
        on_delete=django.db.models.CASCADE,
        null=True,
        verbose_name="иконка",
        related_name="title_image",
    )


class Gallery(AbstractImage):
    """
    model which stores all additional item images
    """

    class Meta:
        verbose_name = "дополнительное фото"
        verbose_name_plural = "дополнительные фото"

    item = django.db.models.ForeignKey(
        Item,
        on_delete=django.db.models.CASCADE,
        default=None,
        related_name="gallery",
    )

    def __str__(self):
        return self.image.url
