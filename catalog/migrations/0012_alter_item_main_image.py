# Generated by Django 3.2.16 on 2023-02-28 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0011_auto_20230228_1712"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="main_image",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="catalog.titleimage",
                verbose_name="иконка",
            ),
        ),
    ]