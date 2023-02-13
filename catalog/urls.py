from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.UIntConverter, "uint")

urlpatterns = [
    path("", views.item_list),
    path("<int:key>/", views.item_detail),
    path("converter/<uint:key>/", views.converter_uint),
    re_path(r"^re/\d*/$", views.re_positive_num),
]
