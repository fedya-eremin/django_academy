from django.http import HttpResponse


def item_list(request):
    return HttpResponse(b"<body>This is item list</body>")


def item_detail(request, key):
    return HttpResponse(f"<body>This is item {key} page</body>".encode("utf-8"))
