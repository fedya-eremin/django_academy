# Generated by Django 3.2.16 on 2023-02-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0005_alter_titleimage_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="titleimage",
            name="image",
            field=models.ImageField(
                blank=True,
                default="../static_dev/img/cat-logo.png",
                null=True,
                upload_to="titles",
            ),
        ),
    ]
