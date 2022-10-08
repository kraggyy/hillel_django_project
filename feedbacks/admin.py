from django.contrib import admin
from feedbacks.models import Feedback


@admin.register(Feedback)
class FeedBackAdmin(admin.ModelAdmin):
    list_filter = ('created_at',)
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
