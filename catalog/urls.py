from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.UIntConverter, "uint")

app_name = "catalog"

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("<int:key>/", views.item_detail, name="item_detail"),
    path("converter/<uint:key>/", views.converter_uint),
    re_path(r"^re/[1-9]+\d*/$", views.re_positive_num),
    path("downloads<path:dst>", views.return_img, name="download"),
]
