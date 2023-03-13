from django.urls import reverse

from feedback.forms import FeedbackForm
from feedback.models import FeedbackModel

import pytest


@pytest.fixture
@pytest.mark.django_db
def feedback_ans(client):
    context = {"form": FeedbackForm()}
    response = client.get(
        reverse("feedback:feedback"),
        data=context,
        follow=True,
    )
    return response.context


def test_form_passed(feedback_ans):
    assert "form" in feedback_ans


def test_form_label_help(feedback_ans):
    assert (
        feedback_ans["form"].fields["text"].label == "Текст"
        and feedback_ans["form"].fields["text"].help_text
        == "Введите текст фидбека"
        and feedback_ans["form"].fields["email"].label == "Почта"
        and feedback_ans["form"].fields["email"].help_text
        == "Введите почтовый адрес"
    )


@pytest.mark.django_db
def test_form_success_redirect(client):
    form_data = {
        "text": "123",
        "email": "dog@ya.ru",
    }
    response = client.post(
        reverse("feedback:feedback"),
        data=form_data,
    )
    assert response.status_code == 302 and response["location"] == reverse(
        "feedback:feedback_success"
    )


@pytest.mark.django_db
def test_form_success_update(client):
    init_cnt = FeedbackModel.objects.count()
    form_data = {
        "text": "123",
        "email": "dog@ya.ru",
    }
    client.post(
        reverse("feedback:feedback"),
        data=form_data,
    )
    final_cnt = FeedbackModel.objects.count()
    assert init_cnt + 1 == final_cnt


@pytest.mark.django_db
def test_form_failing_update(client):
    init_cnt = FeedbackModel.objects.count()
    form_data = {
        "text": "123",
        "email": "ginger.com",
    }
    client.post(
        reverse("feedback:feedback"),
        data=form_data,
    )
    final_cnt = FeedbackModel.objects.count()
    assert init_cnt == final_cnt
