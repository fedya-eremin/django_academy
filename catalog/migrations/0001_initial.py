# Generated by Django 3.2.16 on 2023-02-19 20:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CatalogItem",
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
                ("is_published", models.BooleanField(default=True)),
                ("name", models.TextField(max_length=150)),
                ("text", models.TextField()),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
    ]
