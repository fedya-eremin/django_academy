# Generated by Django 3.2.16 on 2023-02-27 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_titleimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="main_image",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.titleimage",
            ),
        ),
    ]
