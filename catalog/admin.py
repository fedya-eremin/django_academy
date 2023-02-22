from catalog.models import Category, Item, Tag

from django.contrib import admin


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_published",
    )
    list_editable = ("is_published",)
    filter_horizontal = ("tags",)
    list_display_links = ("name",)
    readonly_fields = ["normalized"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = ["normalized"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = ["normalized"]
