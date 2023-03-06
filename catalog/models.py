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

from sorl.thumbnail import get_thumbnail


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


class TitleImage(AbstractImage):
    class Meta:
        verbose_name = "иконка"
        verbose_name_plural = "иконки"


class ItemManager(django.db.models.Manager):
    """
    a simple query manager for Item. I think its functionality is clear
    """

    def mainpage(self):
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
            .filter(is_published=True, is_on_main=True)
        )

    def get_clearly(self, key):
        return get_object_or_404(
            self.get_queryset().only("id", "name", "text", "main_image"),
            id=key,
        )


class Item(AbstractCatalog, NormalizedField):
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

    @property
    def short_text(self):
        return " ".join(self.text.plain.split()[:10])

    is_on_main = django.db.models.BooleanField("На главной", default=False)
    category = django.db.models.ForeignKey(
        Category,
        on_delete=django.db.models.CASCADE,
        default=None,
        verbose_name="категория",
    )
    tags = django.db.models.ManyToManyField(Tag, verbose_name="тэги")

    main_image = django.db.models.OneToOneField(
        TitleImage,
        on_delete=django.db.models.SET_NULL,
        null=True,
        verbose_name="иконка",
    )

    def image_thumbnail(self):
        """shows item's thumbnail on the dashboard of table"""
        if self.main_image:
            thumbnail = get_thumbnail(
                self.main_image.image.path,
                "50x50",
                crop="center",
                quality=51,
            )
            return django.utils.safestring.mark_safe(
                f'<img src="{thumbnail.url}" />'
            )

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "превью"


class Gallery(AbstractImage):
    """
    model which stores all additional item images
    """

    class Meta:
        verbose_name = "допольнительное фото"
        verbose_name_plural = "допольнительные фото"

    item = django.db.models.ForeignKey(
        Item, on_delete=django.db.models.CASCADE, default=None
    )

    def __str__(self):
        return self.image.url
