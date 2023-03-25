from django.contrib import admin

from feedback.models import FeedbackAttachments, FeedbackModel


class AttachmentField(admin.StackedInline):
    model = FeedbackAttachments


@admin.register(FeedbackModel)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (AttachmentField,)
