from http import HTTPStatus

import catalog.models

from django.http import HttpResponse
from django.shortcuts import render

from users.models import Profile


def home(request):
    context = {"items": catalog.models.Item.objects.mainpage()}
    return render(request, "homepage/homepage.html", context)


def coffee(request):
    if request.user.is_authenticated:
        obj = Profile.objects.get(user=request.user)
        obj.coffee_count += 1
        obj.save()
    return HttpResponse(
        "Я - чайник!".encode("utf-8"), status=HTTPStatus.IM_A_TEAPOT
    )


def test_reverse_middleware(request, text):
    return HttpResponse(f"<body>{text}</body>".encode("utf-8"))


def friday(request):
    context = {
        "items": catalog.models.Item.objects.on_friday(),
        "title": "Изменено в пятницу",
    }
    return render(request, "homepage/sidepage.html", context)


def last_week(request):
    context = {
        "items": catalog.models.Item.objects.get_five_random(),
        "title": "Новинки",
    }
    return render(request, "homepage/sidepage.html", context)


def unmodified(request):
    context = {
        "items": catalog.models.Item.objects.not_modified(),
        "title": "Ни разу не изменённые",
    }
    return render(request, "homepage/sidepage.html", context)
