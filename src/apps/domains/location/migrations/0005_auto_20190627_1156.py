# Generated by Django 2.2.2 on 2019-06-27 02:56

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('location', '0004_auto_20190626_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpxpoint',
            name='elevation',
            field=models.FloatField(blank=True, null=True, verbose_name='elevation'),
        ),
        migrations.AlterField(
            model_name='gpxshare',
            name='end_record_time',
            field=models.DateTimeField(blank=True, help_text='종료 시간이 없으면 마지막 데이터까지 공유 됩니다.', null=True, verbose_name='오픈 종료 기록 시간'),
        ),
        migrations.AlterField(
            model_name='gpxshare',
            name='share_uuid',
            field=models.UUIDField(default=uuid.UUID('bf9d72b4-f7c4-4b94-bb64-02962631563b'), unique=True, verbose_name='공유 UUID'),
        ),
    ]
