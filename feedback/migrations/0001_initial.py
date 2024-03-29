# Generated by Django 3.2.16 on 2023-03-14 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ComplainingUserModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Имя")),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="Почта"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeedbackModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Сообщение")),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("received", "Получено"),
                            ("processing", "В обработке"),
                            ("answered", "Ответ дан"),
                        ],
                        default="received",
                        max_length=15,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="feedback.complainingusermodel",
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Обратная связь",
                "verbose_name_plural": "Обратные связи",
            },
        ),
    ]
