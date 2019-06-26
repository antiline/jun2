from django.contrib import admin

from apps.domains.location.models.models import GpxPoint


@admin.register(GpxPoint)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'record_time', 'latitude', 'longitude', 'elevation', 'create_time', 'update_time',)
    list_display_links = ('user', 'record_time',)
    list_filter = ('record_time', 'update_time',)
    search_fields = ('user',)
