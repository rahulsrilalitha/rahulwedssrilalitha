from django.contrib import admin
from .models import Engagement


# Register your models here.

class EngagementAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'image_tag')
    list_filter = ('uploaded_at',)
    search_fields = ('title',)


admin.site.register(Engagement, EngagementAdmin)
