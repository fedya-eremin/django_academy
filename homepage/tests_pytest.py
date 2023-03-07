from catalog.models import Category, Item

import django.urls
from django.test import Client

import pytest


@pytest.mark.django_db
def test_mainpage_occurency(db):
    response = Client().get(django.urls.reverse("homepage:home"))
    ans = "items" in response.context
    assert ans is True


@pytest.mark.django_db
def test_mainpage_item_amount(db):
    category = Category.objects.create(id=1, name="Fruits")
    Item.objects.create(
        id=100,
        name="test_item",
        is_published=True,
        category=category,
        is_on_main=True,
    )
    response = Client().get(django.urls.reverse("homepage:home"))
    assert response.context["items"].count() == 1
