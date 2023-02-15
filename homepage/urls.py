from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("coffee", views.coffee),
    path("test/<path:text>", views.test_reverse_middleware),
]
