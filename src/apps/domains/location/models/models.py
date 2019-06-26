from django.contrib.auth.models import User
from django.db import models

from libs.django.db.models.base_model import BaseModel


class Gpx(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='user')
    record_time = models.DateTimeField(null=False, verbose_name='기록 시간')
    latitude = models.FloatField(null=False, verbose_name='latitude')
    longitude = models.FloatField(null=False, verbose_name='longitude')
    elevation = models.FloatField(null=False, verbose_name='elevation')

    class Meta:
        db_table = 'gpx'
        verbose_name = 'GPX'
        verbose_name_plural = 'GPX 리스트'

    def __str__(self):
        return '%s - %s' % (self.user, self.record_time)
