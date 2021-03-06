# Generated by Django 2.2.2 on 2019-07-20 21:28

from django.db import migrations, models
import libs.django.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_auto_20190721_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractgpsfromexifstatus',
            name='image_path',
            field=libs.django.db.fields.RelativeFilePathField(allow_files=False, allow_folders=True, path='/Users/antiline/Documents/Jun2/jun2/mount', recursive=True, verbose_name='Image 경로'),
        ),
        migrations.AlterField(
            model_name='gpxshare',
            name='share_uuid',
            field=models.UUIDField(default=uuid.UUID('13121f7a-c660-47fa-92b6-25687c8f7c21'), unique=True, verbose_name='공유 UUID'),
        ),
    ]
