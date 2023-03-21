import django.db.models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

from myserver.settings import NEW_USER_ACTIVATED


def gen_user_path(instance, filename):
    return f"users/{instance.user.id}/{filename}"


@receiver(pre_save, sender=User)
def default_user_inactive(sender, instance, update_fields, **kwargs):
    if instance._state.adding is True and NEW_USER_ACTIVATED is False:
        instance.is_active = False


class Profile(django.db.models.Model):
    """
    extends django's User with DOB, image & coffee count
    """

    class Meta:
        verbose_name = "профиль"
        verbose_name_plural = "профили"

    user = django.db.models.OneToOneField(
        User,
        on_delete=django.db.models.CASCADE,
    )
    birthday = django.db.models.DateField(
        "дата рождения", blank=True, null=True, default=None
    )

    image = django.db.models.ImageField(
        "аватарка",
        upload_to=gen_user_path,
        default="cat-logo.png",
    )

    coffee_count = django.db.models.PositiveBigIntegerField(
        "сварено кофе",
        default=0,
    )
