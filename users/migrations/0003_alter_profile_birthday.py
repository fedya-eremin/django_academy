# Generated by Django 3.2.16 on 2023-03-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_auto_20230319_1702"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="birthday",
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]