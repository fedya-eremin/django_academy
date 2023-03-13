from django.contrib import admin

from feedback.models import FeedbackModel


@admin.register(FeedbackModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("email",)
