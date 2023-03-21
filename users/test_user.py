from datetime import datetime

from django.contrib.auth.models import User
from django.urls import reverse

import pytest

NOT_NOW = datetime(2099, 11, 11, 11)


def mocked_time():
    return NOT_NOW


@pytest.mark.django_db
class TestUser:
    # по неизвестной мне причине я не могу мокать настройки
    # что с unittest, что и с pytest
    # фикстутра работает, но что то пользователь все равно активен
    @pytest.fixture(autouse=True)
    def setup(self, settings):
        settings.DEBUG = False
        settings.NEW_USER_ACTIVATED = False

    @pytest.fixture
    def inactive_user(self, client):
        context = {
            "username": "new_user",
            "password1": "yandexbrowser12",
            "password2": "yandexbrowser12",
        }
        response1 = client.post(
            reverse("users:signup"),
            data=context,
        )

        a = User.objects.get(pk=1)
        a.is_active = False
        a.save()
        response2 = client.get(
            reverse("users:activation_view", args=[context["username"]])
        )

        return response1, response2

    def test_user_reg_and_activate(self, inactive_user):
        assert (
            inactive_user[0].status_code == 302
            and inactive_user[1].status_code == 302
        )
