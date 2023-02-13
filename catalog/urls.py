from django.urls import path

from . import views

urlpatterns = [
    path("", views.item_list),
    path("<int:key>/", views.item_detail),
]
