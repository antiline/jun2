from django.contrib.auth.models import User
from django.db import models

from libs.django.db.models.base_model import BaseModel


class GpxPoint(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='user')
    record_time = models.DateTimeField(null=False, verbose_name='기록 시간')
    latitude = models.FloatField(null=False, verbose_name='latitude')
    longitude = models.FloatField(null=False, verbose_name='longitude')
    elevation = models.FloatField(null=False, verbose_name='elevation')

    class Meta:
        db_table = 'gpx_point'
        verbose_name = 'GPX Point'
        verbose_name_plural = 'GPX Point 리스트'
        unique_together = (('user', 'record_time'),)

    def change(self, latitude: float, longitude: float, elevation: float):
        return self._change(latitude=latitude, longitude=longitude, elevation=elevation)
