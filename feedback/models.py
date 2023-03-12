import django.db.models


class FeedbackModel(django.db.models.Model):
    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратные связи"

    text = django.db.models.TextField("Сообщение")
    created_on = django.db.models.DateTimeField(auto_now_add=True)
    email = django.db.models.EmailField("Почта")
