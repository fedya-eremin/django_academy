import django.db.models


class ComplainingUserModel(django.db.models.Model):
    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    name = django.db.models.CharField("Имя", max_length=50)
    email = django.db.models.EmailField("Почта")


class FeedbackModel(django.db.models.Model):
    class Meta:
        verbose_name = "обратная связь"
        verbose_name_plural = "обратные связи"

    text = django.db.models.TextField("Сообщение")
    created_on = django.db.models.DateTimeField(auto_now_add=True)
    author = django.db.models.ForeignKey(
        ComplainingUserModel,
        on_delete=django.db.models.DO_NOTHING,
        default=None,
        verbose_name="Автор",
    )

    class FeedbackStatus(django.db.models.TextChoices):
        RECEIVED = "received", "Получено"
        PROCESSING = "processing", "В обработке"
        ANSWERED = "answered", "Ответ дан"

    status = django.db.models.CharField(
        max_length=15,
        choices=FeedbackStatus.choices,
        default=FeedbackStatus.RECEIVED,
        verbose_name="Статус",
    )

    def __str__(self):
        return self.author.email


def attachment_handler(instance, filename):
    return f"attachments/{instance.feedback.id}/{filename}"


class FeedbackAttachments(django.db.models.Model):
    class Meta:
        verbose_name = "вложение"
        verbose_name_plural = "вложения"

    feedback = django.db.models.ForeignKey(
        FeedbackModel,
        on_delete=django.db.models.CASCADE,
        default=None,
        related_name="attachment",
    )

    file = django.db.models.FileField("Вложение", upload_to=attachment_handler)
