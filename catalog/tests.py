from catalog.models import (
    CatalogCategory,
    CatalogItem,
    CatalogTag,
    great_validator,
)

import django.core.exceptions

import pytest


def test_catalog_endpoint(client):
    assert client.get("/catalog/").status_code == 200


@pytest.mark.parametrize(
    "url,code",
    [
        (123, 200),
        (12345, 200),
        (100, 200),
        (200, 200),
        (0, 200),
        (3.1415, 404),
        (-5, 404),
        ("test", 404),
        ("string", 404),
        (None, 404),
        (True, 404),
    ],
)
def test_catalog_number_endpoint(url, code, client):
    assert client.get(f"/catalog/{url}/").status_code == code


@pytest.mark.parametrize(
    "url,code",
    [
        (123, 200),
        (456, 200),
        (789, 200),
        ("012", 404),
        (0x012, 200),
        (0, 404),
        ("0x012", 404),
        ("string", 404),
        (1.4142, 404),
        (True, 404),
        (None, 404),
    ],
)
def test_re_number_endpoint(url, code, client):
    assert client.get(f"/catalog/re/{url}/").status_code == code


@pytest.mark.parametrize(
    "url,code",
    [
        (123, 200),
        (456, 200),
        (789, 200),
        ("012", 404),
        (0x012, 200),
        (0, 404),
        ("0x012", 404),
        ("string", 404),
        (1.4142, 404),
        (True, 404),
        (None, 404),
    ],
)
def test_converter_uint_endpoint(url, code, client):
    assert client.get(f"/catalog/converter/{url}/").status_code == code


@pytest.fixture
def category(db):
    return CatalogCategory.objects.create(name="test_category")


def test_category_creation(category):
    assert category.name == "test_category"


@pytest.fixture
def tag(db):
    return CatalogTag.objects.create(name="test_tag")


def test_tag_creation(tag):
    assert tag.name == "test_tag"


@pytest.mark.parametrize(
    "text",
    [
        "qweqweq",
        "123123213123",
        "ogqweqqыфвфф",
        "яндексбраузер",
    ],
)
def test_great_validator_negative(text):
    with pytest.raises(django.core.exceptions.ValidationError):
        great_validator(text)


@pytest.mark.parametrize(
    "text",
    [
        "яндекс бразер - это превосходно",
        "пользоваться им - роскошно",
        "превосходно роскошно",
    ],
)
def test_great_validator_positive(text):
    assert great_validator(text) is None
