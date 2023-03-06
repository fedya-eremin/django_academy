import catalog.models

from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    context = {"items": catalog.models.Item.objects.mainpage()}
    return render(request, "catalog/catalog.html", context)


def item_detail(request, key):
    context = {
        "item": catalog.models.Item.objects.get(id=key),
        "gallery": catalog.models.Gallery.objects.filter(item=key),
    }
    return render(request, "catalog/item.html", context)


def re_positive_num(request):
    return HttpResponse(
        b"<body>This is re page which handles positive number</body>"
    )


def converter_uint(request, key):
    return HttpResponse(f"<body>Used converter {key}</body>".encode("utf-8"))
