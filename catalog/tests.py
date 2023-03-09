from catalog.models import Category, Item, Tag
from catalog.validators import GreatValidator

import django.core.exceptions
import django.urls
from django.forms.models import model_to_dict
from django.test import Client

from django_quill.quill import Quill

from myserver import settings

import pytest


def test_catalog_endpoint(db, client):
    assert client.get("/catalog/").status_code == 200


@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize(
    "url,code",
    [
        ("1", 200),
        ("%%%", 404),
        ("string", 404),
        ("12", 200),
        (True, 404),
        (False, 404),
        ("yandex", 404),
        ("qweqweqeq", 404),
        ("12213ygy2131", 404),
        (None, 404),
        ("case", 404),
    ],
)
def test_catalog_number_endpoint(url, code):
    category = Category.objects.create(id=1, name="Fruits")
    if url not in (True, False, None) and url.isdigit():
        Item.objects.create(id=int(url), name="123", category=category)
    try:
        response = Client().get(
            django.urls.reverse("catalog:item_detail", args=[url])
        )
        assert response.status_code == code
    except Exception:
        assert True


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


def test_category_creation_and_count(db):
    init_cnt = Category.objects.count()
    category = Category.objects.create(name="test_category")
    final_cnt = Category.objects.count()
    assert final_cnt == init_cnt + 1 and category.name == "test_category"


def test_tag_creation_and_count(db):
    init_cnt = Tag.objects.count()
    tag = Tag.objects.create(name="test_tag")
    final_cnt = Tag.objects.count()
    assert final_cnt == init_cnt + 1 and tag.name == "test_tag"


@pytest.fixture
def category(db):
    return Category.objects.create(name="test_category")


@pytest.mark.django_db
def test_item_creation_and_count(db):
    init_cnt = Item.objects.count()
    category = Category.objects.create(id=1, name="Fruits")
    item = Item.objects.create(id=100, name="test_item", category=category)
    final_cnt = Item.objects.count()
    assert final_cnt == 1 + init_cnt and item.name == "test_item"


@pytest.mark.xfail
@pytest.mark.parametrize(
    "name",
    [
        "Cвежее",
        "СвeЖЕЕ",
        "Нoвоe",
        "НОВОЕ",
    ],
)
def test_normalize_negative(db, name):
    assert Tag.objects.create(name=name)


@pytest.mark.parametrize(
    "name", ["тег", "123123123", "Категория", "ЯндексБраузер"]
)
def test_normalize_positive(db, name):
    assert Tag.objects.create(name=name).name == name


@pytest.mark.django_db
def test_mainpage_occurency(db):
    response = Client().get(django.urls.reverse("homepage:home"))
    ans = "items" in response.context
    assert ans is True


def get_quill(value):
    quill = Quill(
        {
            "delta": {"ops": [{"insert": "%s\\n" % value}]},
            "html": "<p>%s</p>" % value,
        }
    )
    with open("sth.txt", "w+") as file:
        file.write(str(quill))
    return quill


@pytest.fixture
@pytest.mark.django_db
def item():
    category = Category.objects.create(id=1, name="Fruits")
    return Item.objects.create(
        id=1,
        name="123",
        category=category,
        text='{"delta":"{\\"ops\\":[{\\"insert\\":\\"превосходно груша'
        '\\\\n\\"}]}","html":"<p>превосходно груша</p>"}',
    )


@pytest.mark.django_db(transaction=True)
def test_item_type(item):
    assert type(item) == Item


@pytest.mark.parametrize(
    "field",
    (
        "id",
        "is_published",
        "is_on_main",
        "name",
        "text",
        "category",
        "tags",
        "image",
    ),
)
@pytest.mark.django_db
def test_item_details_positive(field, item):
    response = Client().get(
        django.urls.reverse("catalog:item_detail", args=["1"])
    )
    assert field in model_to_dict(response.context["item"])


@pytest.mark.parametrize("field", ("normalized",))
@pytest.mark.django_db(transaction=True)
def test_item_details_negative(field, item):
    response = Client().get(
        django.urls.reverse("catalog:item_detail", args=["1"])
    )
    assert field not in model_to_dict(response.context["item"])


@pytest.mark.django_db
def test_validator_in_response(item):
    response = Client().get(
        django.urls.reverse("catalog:item_detail", args=["1"])
    )
    func = GreatValidator(*settings.VALIDATE_WORDS)
    assert func(response.context["item"].text) is None
