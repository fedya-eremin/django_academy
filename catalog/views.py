from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    return render(request, "catalog/catalog.html")


def item_detail(request, key):
    return render(request, "catalog/item.html")


def re_positive_num(request):
    return HttpResponse(
        b"<body>This is re page which handles positive number</body>"
    )


def converter_uint(request, key):
    return HttpResponse(f"<body>Used converter {key}</body>".encode("utf-8"))
