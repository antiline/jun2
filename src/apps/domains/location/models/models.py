import uuid
from typing import Optional

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from libs.django.db.models.base_model import BaseModel


class GpxPoint(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='user')
    record_time = models.DateTimeField(null=False, verbose_name='기록 시간')
    latitude = models.FloatField(null=False, verbose_name='latitude')
    longitude = models.FloatField(null=False, verbose_name='longitude')
    elevation = models.FloatField(null=True, blank=True, verbose_name='elevation')

    class Meta:
        db_table = 'gpx_point'
        verbose_name = 'GPX Point'
        verbose_name_plural = 'GPX Point 리스트'
        unique_together = (('user', 'record_time'),)

    def change(self, latitude: float, longitude: float, elevation: Optional[float]):
        return self._change(latitude=latitude, longitude=longitude, elevation=elevation)


class GpxShare(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='user')
    share_uuid = models.UUIDField(unique=True, default=uuid.uuid4(), verbose_name='공유 UUID')
    is_active = models.BooleanField(null=False, default=True, verbose_name='활성화 여부')
    start_record_time = models.DateTimeField(null=False, verbose_name='오픈 시작 기록 시간')
    end_record_time = models.DateTimeField(
        null=True, blank=True, verbose_name='오픈 종료 기록 시간', help_text='종료 시간이 없으면 마지막 데이터까지 공유 됩니다.'
    )

    class Meta:
        db_table = 'gpx_share'
        verbose_name = 'GPX Share'
        verbose_name_plural = 'GPX Share 리스트'


class GpxCrawlStatus(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='user')
    is_active = models.BooleanField(null=False, default=True, verbose_name='활성화 여부')
    crawl_url = models.URLField(null=False, verbose_name='Crawl URL')

    class Meta:
        db_table = 'gpx_crawl_status'
        verbose_name = 'GPX Crawl Status'
        verbose_name_plural = 'GPX Crawl Status 리스트'


class ExtractGpsFromExifStatus(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='user')
    is_active = models.BooleanField(null=False, default=True, verbose_name='활성화 여부')
    image_path = models.FilePathField(
        path=settings.MOUNT_PATH, allow_folders=True, allow_files=False, recursive=True, verbose_name='Image 경로'
    )

    class Meta:
        db_table = 'extract_gps_from_exif_status'
        verbose_name = 'Exif 에서 GPS 정보 가져오기 상태'
        verbose_name_plural = 'Exif 에서 GPS 정보 가져오기 상태 리스트'

