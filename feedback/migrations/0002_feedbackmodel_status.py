# Generated by Django 3.2.16 on 2023-03-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feedback", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedbackmodel",
            name="status",
            field=models.CharField(
                choices=[
                    ("Получено", "Received"),
                    ("В обработке", "Processing"),
                    ("Ответ дан", "Answered"),
                ],
                default="Получено",
                max_length=15,
            ),
        ),
    ]