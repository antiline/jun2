from django.contrib import admin

from apps.domains.location.models.models import GpxCrawlStatus, GpxPoint, GpxShare, ExtractGpsOnExifStatus


@admin.register(GpxPoint)
class GpxPointAdmin(admin.ModelAdmin):
    list_display = ('user', 'record_time', 'latitude', 'longitude', 'elevation', 'create_time', 'update_time',)
    list_display_links = ('user', 'record_time',)
    list_filter = ('record_time', 'update_time',)
    search_fields = ('user',)


@admin.register(GpxShare)
class GpxShareAdmin(admin.ModelAdmin):
    list_display = ('user', 'share_uuid', 'start_record_time', 'end_record_time', 'create_time', 'update_time',)
    list_display_links = ('user', 'share_uuid',)
    list_filter = ('start_record_time', 'end_record_time',)
    search_fields = ('user', 'share_uuid',)


@admin.register(GpxCrawlStatus)
class GpxCrawlStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'crawl_url', 'is_active', 'create_time', 'update_time',)
    list_display_links = ('user', 'crawl_url',)
    list_filter = ('is_active',)
    search_fields = ('user',)


@admin.register(ExtractGpsOnExifStatus)
class ExtractGpsOnExifStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_path', 'is_active', 'create_time', 'update_time',)
    list_display_links = ('user', 'image_path',)
    list_filter = ('is_active',)
    search_fields = ('user',)
