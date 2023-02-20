from catalog.models import CatalogCategory, CatalogItem, CatalogTag

from django.contrib import admin


@admin.register(CatalogItem)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_published",
    )
    list_editable = ("is_published",)
    filter_horizontal = ("tags",)
    list_display_links = ("name",)


@admin.register(CatalogCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(CatalogTag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
