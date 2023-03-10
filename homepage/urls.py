from django.urls import path

from . import views

app_name = "homepage"

urlpatterns = [
    path("", views.home, name="home"),
    path("coffee", views.coffee),
    path("test/<path:text>", views.test_reverse_middleware),
    path("friday/", views.friday, name="friday"),
    path("last-week/", views.last_week, name="last_week"),
    path("unmodified/", views.unmodified, name="unmodified"),
]
