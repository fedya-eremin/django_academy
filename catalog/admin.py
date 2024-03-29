from catalog.models import Category, Gallery, Item, Tag, TitleImage

from django.contrib import admin


class GalleryField(admin.StackedInline):
    model = Gallery
    extra = 1


class TitleImageField(admin.StackedInline):
    model = TitleImage
    min_num = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    class Meta:
        model = Item

    list_display = (
        "name",
        "is_published",
        "image_thumbnail",
        "date_modified",
        "date_published",
        "is_modified",
    )
    inlines = (GalleryField, TitleImageField)
    list_editable = ("is_published",)
    filter_horizontal = ("tags",)
    list_display_links = ("name",)
    readonly_fields = ("normalized", "image_thumbnail")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = ["normalized"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = ["normalized"]
