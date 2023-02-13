from django.http import HttpResponse


def home(request):
    return HttpResponse(b"<body>This is homepage</body>")


def coffee(request):
    response = HttpResponse("Я - чайник!")
    response.status_code = 418
    return response
