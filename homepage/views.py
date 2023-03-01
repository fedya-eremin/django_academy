from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "homepage/homepage.html")


def coffee(request):
    return HttpResponse(
        "Я - чайник!".encode("utf-8"), status=HTTPStatus.IM_A_TEAPOT
    )


def test_reverse_middleware(request, text):
    return HttpResponse(f"<body>{text}</body>".encode("utf-8"))
