import django.db.models
from django.core.exceptions import ValidationError


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

    def __str__(self):
        return self.name


class NormalizedField(django.db.models.Model):
    class Meta:
        abstract = True
        verbose_name = "нормализовано"
        verbose_name_plural = "нормализовано"

    normalized = django.db.models.TextField(
        default="", unique=True, editable=False
    )
    name = AbstractCatalog.__dict__["name"]

    def clean(self, *args, **kwargs):
        """
        если честно, я не представляю, как сделать это иначе, кроме как
        переопределяя save() или clean(). Оба они возвращают цикл исключений
        при попытке внести похожее на уже существующее значение :(
        """
        alph_ru = "АВЕКМНОРСТХаеомнкрстух"
        alph_en = "ABEKMНOPCTXaeomhkpctyx"
        puncts = ",.!?:;'\""
        normalized = ""
        for i in self.name.split():
            if i in alph_ru:
                normalized += alph_en[alph_ru.index(i)]
            elif i in puncts:
                normalized += "."
            else:
                normalized += i
        self.normalized = normalized.lower()
        manager = self.__class__.objects.all()
        if len(manager.filter(normalized=self.normalized).exclude(id=self.id)):
            raise ValidationError("Поле с подобным именем уже имеется!")
        super(NormalizedField, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.clean()
        super(NormalizedField, self).save(*args, **kwargs)


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


class AbstractImage(django.db.models.Model):
    """
    abstract model of o2m ImageField which
    SAVES EVERYTHING TO media/gallery
    """

    class Meta:
        abstract = True

    image = django.db.models.ImageField(
        "Изображение",
        upload_to="gallery",
        default="../static_dev/img/cat-logo.png",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.image.path
