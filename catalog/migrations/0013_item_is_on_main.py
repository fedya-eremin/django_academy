# Generated by Django 3.2.16 on 2023-03-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0012_alter_item_main_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="is_on_main",
            field=models.BooleanField(
                default=False, verbose_name="На главной"
            ),
        ),
    ]