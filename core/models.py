import django.db.models


class AbstractCatalog(django.db.models.Model):
    """
    a parent to other models. has is_published checkbox,
    name with max_length 150
    """

    class Meta:
        abstract = True
        verbose_name = "абстрактная модель"
        verbose_name_plural = "абстрактные модели"

    is_published = django.db.models.BooleanField(default=True)
    name = django.db.models.TextField(
        max_length=150, help_text="Имя, содержит до 150 символов"
    )
