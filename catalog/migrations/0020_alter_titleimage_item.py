# Generated by Django 3.2.16 on 2023-03-13 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0019_auto_20230310_0816"),
    ]

    operations = [
        migrations.AlterField(
            model_name="titleimage",
            name="item",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="title_image",
                to="catalog.item",
                verbose_name="иконка",
            ),
        ),
    ]
