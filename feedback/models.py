import django.db.models


class FeedbackModel(django.db.models.Model):
    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратные связи"

    def __str__(self):
        return self.email

    text = django.db.models.TextField("Сообщение")
    created_on = django.db.models.DateTimeField(auto_now_add=True)
    email = django.db.models.EmailField("Почта")

    class FeedbackStatus(django.db.models.TextChoices):
        RECEIVED = "received", "Получено"
        PROCESSING = "processing", "В обработке"
        ANSWERED = "answered", "Ответ дан"

    status = django.db.models.CharField(
        max_length=15,
        choices=FeedbackStatus.choices,
        default=FeedbackStatus.RECEIVED,
    )
