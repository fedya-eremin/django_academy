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

from django_quill.fields import QuillField

from sorl.thumbnail.engines.pil_engine import Engine


def crop_image(fin):
    """
    crops image via sorl pil_engine and returns
    its object (for any purpose)
    """
    with open(fin, "rb") as file:
        rat = Engine().get_image(file)
    resized = Engine().crop(rat, (300, 300), options={"crop": "center"})
    resized.save(fin)
    return resized


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


class TitleImage(django.db.models.Model):
    class Meta:
        verbose_name = "иконка"
        verbose_name_plural = "иконки"

    image = django.db.models.ImageField(
        "Иконка",
        upload_to="titles",
        default="../static_dev/img/cat-logo.png",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.image.path


class Item(AbstractCatalog, NormalizedField):
    """
    model which describes item.
    has AbstractCatalog's inner fields, text,
    category(one-to-many), tags(many-to-many)
    """

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    text = QuillField(
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

    main_image = django.db.models.OneToOneField(
        TitleImage,
        on_delete=django.db.models.CASCADE,
        null=True,
        verbose_name="иконка",
    )

    def image_thumbnail(self):
        """shows item's thumbnail on the dashboard of table"""
        if self.main_image:
            return django.utils.safestring.mark_safe(
                f'<img src="{self.main_image.image.url}" height=50>'
            )

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "превью"

    def save(self, *args, **kwargs):
        self.clean()

        super(Item, self).save(*args, **kwargs)  # needed if image is abscent
        try:
            crop_image(self.main_image.image.path)
        except ValueError:  # suppresses warning on deletion
            pass
        super(Item, self).save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        # same as item, except clean()
        super(Gallery, self).save(
            *args, **kwargs
        )  # needed if image is abscent
        try:
            crop_image(self.image.path)
        except ValueError:  # suppresses exception on deletion
            pass
        super(Gallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.image.url
