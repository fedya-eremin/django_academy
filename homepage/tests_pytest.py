import django.urls
from django.test import Client

import pytest


@pytest.mark.django_db
def test_mainpage_occurency(db):
    response = Client().get(django.urls.reverse("homepage:home"))
    ans = "items" in response.context
    assert ans is True
