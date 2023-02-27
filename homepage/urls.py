from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "homepage"

urlpatterns = [
    path("", views.home, name="home"),
    path("coffee", views.coffee),
    path("test/<path:text>", views.test_reverse_middleware),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
