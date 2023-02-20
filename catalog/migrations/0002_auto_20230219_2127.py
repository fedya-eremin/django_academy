# Generated by Django 3.2.16 on 2023-02-19 21:27

import catalog.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('name', models.TextField(max_length=150)),
                ('slug', models.TextField(max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='Слизняк')),
                ('weight', models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(32767)], verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='CatalogTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('name', models.TextField(max_length=150)),
                ('slug', models.TextField(max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='Слизняк')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AlterField(
            model_name='catalogitem',
            name='text',
            field=models.TextField(validators=[catalog.models.great_validator], verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.catalogcategory'),
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='tags',
            field=models.ManyToManyField(to='catalog.CatalogTag'),
        ),
    ]
