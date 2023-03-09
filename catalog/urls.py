from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.UIntConverter, "uint")

app_name = "catalog"

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("<int:key>/", views.item_detail, name="item_detail"),
    path("converter/<uint:key>/", views.converter_uint),
    re_path(r"^re/[1-9]+\d*/$", views.re_positive_num),
    path("friday/", views.friday, name="friday"),
    path("last-week/", views.last_week, name="last_week"),
    path("unmodified/", views.unmodified, name="unmodified"),
    # needs to be last
    path("<path:dst>/", views.return_img, name="download"),
]
