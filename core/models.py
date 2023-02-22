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

    is_published = django.db.models.BooleanField("Опубликовано", default=True)
    name = django.db.models.TextField(
        "Имя", max_length=150, help_text="Имя, содержит до 150 символов"
    )
    normalized = django.db.models.TextField(
        default="", unique=True, editable=False
    )

    def save(self, *args, **kwargs):
        """
        если честно, я не представляю, как сделать это иначе, кроме как
        переопределяя save() или clean(). Оба они возвращают цикл исключений
        при попытке внести похожее на уже существующее значение :(
        """
        alph_ru = "АВЕКМОРСТХаеорсух"
        alph_en = "ABEKMOPCTXaeopcyx"
        puncts = ",.!?:;'\""
        normalized = ""
        # name = self.name
        for i in self.name.split():
            if i in alph_ru:
                normalized += alph_en[alph_ru.index(i)]
            elif i in puncts:
                normalized += "."
            else:
                normalized += i
        self.normalized = normalized.lower()
        super(AbstractCatalog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class AbstractWithSlug(django.db.models.Model):
    class Meta:
        abstract = True
        verbose_name = "модель со slug"
        verbose_name_plural = "модели со slug"

    slug = django.db.models.SlugField(
        "Слизняк",
        unique=True,
        max_length=200,
        help_text="Впишите slug-последовательность в поле",
    )
