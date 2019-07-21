# Generated by Django 2.2.2 on 2019-07-21 16:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0009_auto_20190722_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpxpoint',
            name='ref_type',
            field=models.IntegerField(choices=[(0, 'GPX crawl'), (1, 'Extract from exif'), (2, 'by User')], verbose_name='Point reference 타입'),
        ),
        migrations.AlterField(
            model_name='gpxshare',
            name='share_uuid',
            field=models.UUIDField(default=uuid.UUID('d3a4a4f5-8641-4170-aa5f-703c2aea4628'), unique=True, verbose_name='공유 UUID'),
        ),
    ]