# Generated by Django 3.2.16 on 2023-02-26 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'допольнительное фото', 'verbose_name_plural': 'допольнительные фото'},
        ),
    ]
