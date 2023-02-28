# Generated by Django 3.2.16 on 2023-02-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0010_auto_20230228_1318"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="image",
            field=models.ImageField(
                default="../static_dev/img/cat-logo.png",
                upload_to="gallery",
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="titleimage",
            name="image",
            field=models.ImageField(
                default="../static_dev/img/cat-logo.png",
                upload_to="gallery",
                verbose_name="Изображение",
            ),
        ),
    ]
