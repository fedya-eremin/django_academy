from django.http import HttpResponse


def home(request):
    return HttpResponse(b"<body>This is homepage</body>")
