import django.db.models


class AbstractCatalog(django.db.models.Model):
    """
    a parent to other models. has is_published checkbox,
    name with max_length 150
    """

    class Meta:
        abstract = True

    is_published = django.db.models.BooleanField(default=True)
    name = django.db.models.TextField(max_length=150)
