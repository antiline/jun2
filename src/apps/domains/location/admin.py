from django.contrib import admin

from apps.domains.location.models.models import Gpx


@admin.register(Gpx)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'record_time', 'latitude', 'longitude', 'elevation', 'created', 'last_modified',)
    list_display_links = ('user', 'record_time',)
    list_filter = ('record_time', 'last_modified',)
    search_fields = ('user',)
