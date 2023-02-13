from http import HTTPStatus

from django.http import HttpResponse


def home(request):
    return HttpResponse(b"<body>This is homepage</body>")


def coffee(request):
    return HttpResponse(
        "Я - чайник!".encode("utf-8"), status=HTTPStatus.IM_A_TEAPOT
    )
