from django.http import HttpResponse


def description(request):
    return HttpResponse(b"<body>This is website description</body>")

