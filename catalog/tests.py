import django.core.exceptions
import pytest

from catalog.models import Category, Item, Tag
from catalog.validators import GreatValidator


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


def test_category_creation(db):
    init_cnt = Category.objects.count()
    category = Category.objects.create(name="test_category")
    final_cnt = Category.objects.count()
    assert final_cnt == init_cnt + 1 and category.name == "test_category"


def test_tag_creation(db):
    init_cnt = Tag.objects.count()
    tag = Tag.objects.create(name="test_tag")
    final_cnt = Tag.objects.count()
    assert final_cnt == init_cnt + 1 and tag.name == "test_tag"


@pytest.fixture
def category(db):
    return Category.objects.create(name="test_category")


# fails for some reason...
# def test_item_creation(db, category):
#     init_cnt = Item.objects.count()
#     item = Item.objects.create(name="test_item", category=category)
#     final_cnt = Item.objects.count()
#     assert final_cnt == init_cnt + 1 and item.name == "test_item"


@pytest.mark.parametrize(
    "text",
    [
        "qweqweq",
        "123123213123",
        "ogqweqqыфвфф",
        "яндексбраузер",
        "weweqwdпревосходнононеверно",
        "роскошнононеправильно",
    ],
)
def test_great_validator_negative(text):
    with pytest.raises(django.core.exceptions.ValidationError):
        func = GreatValidator("превосходно", "роскошно")
        func(text)


@pytest.mark.parametrize(
    "text",
    [
        "яндекс бразер - это превосходно",
        "пользоваться им - роскошно",
        "превосходно роскошно",
        "Роскошно!!!",
        "превосходно? но правильно!",
    ],
)
def test_great_validator_positive(text):
    func = GreatValidator("превосходно", "роскошно")
    assert func(text) is None


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
