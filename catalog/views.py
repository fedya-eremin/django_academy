from django.http import HttpResponse


def item_list(request):
    return HttpResponse(b"<body>This is item list</body>")


def item_detail(request, key):
    return HttpResponse(f"<body>This is item {key}</body>".encode("utf-8"))


def re_positive_num(request):
    return HttpResponse(
        b"<body>This is re page which handles positive number</body>"
    )


def converter_uint(request, key):
    return HttpResponse(f"<body>Used converter {key}</body>".encode("utf-8"))
