from datetime import date, timedelta

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
from django.db.models import F
from django.shortcuts import get_object_or_404


from django_quill.fields import QuillField

from myserver import settings


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
            .only("name", "text", "title_image", "category", "tags"),
            pk=key,
        )

    def not_modified(self):
        return self.base_query().filter(
            date_modified__year=F("date_published__year"),
            date_modified__month=F("date_published__month"),
            date_modified__day=F("date_published__day"),
            date_modified__hour=F("date_published__hour"),
            date_modified__minute=F("date_published__minute"),
            date_modified__second=F("date_published__second"),
        )

    def on_friday(self):
        return self.base_query().filter(date_modified__iso_week_day=5)

    def get_five_random(self):
        return (
            self.base_query()
            .filter(date_published__date__gte=date.today() - timedelta(days=7))
            .order_by("?")[:5]
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
            GreatValidator(*settings.VALIDATE_WORDS),
        ],
        help_text='Текст должен содержать слово "превосходно" или "роскошно"',
    )
    date_modified = django.db.models.DateTimeField(
        "время изменения", auto_now=True
    )
    date_published = django.db.models.DateTimeField(
        "время публикации", auto_now_add=True
    )

    is_on_main = django.db.models.BooleanField("На главной", default=False)
    category = django.db.models.ForeignKey(
        Category,
        on_delete=django.db.models.CASCADE,
        default=None,
        verbose_name="категория",
    )
    tags = django.db.models.ManyToManyField(Tag, verbose_name="тэги")

    @property  # move it to manager's annotation
    def is_modified(self):
        if int(self.date_modified.strftime("%Y%m%d%H%M%S")) == int(
            self.date_published.strftime("%Y%m%d%H%M%S")
        ):
            return False
        return True

    def image_thumbnail(self):
        """shows item's thumbnail on the dashboard of table"""
        if self.title_image.image:
            return django.utils.safestring.mark_safe(
                f'<img src="{self.title_image.get_thumb_50x50.url}" />'
            )
        return "no title image"

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "превью"


class TitleImage(AbstractImage):
    class Meta:
        verbose_name = "иконка"
        verbose_name_plural = "иконки"

    item = django.db.models.OneToOneField(
        Item,
        on_delete=django.db.models.CASCADE,
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
