# Generated by Django 2.2.1 on 2019-06-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('location', '0002_gpxcrawlstatus_gpxshare'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gpxshare',
            options={'verbose_name': 'GPX Share', 'verbose_name_plural': 'GPX Share 리스트'},
        ),
        migrations.AlterField(
            model_name='gpxcrawlstatus',
            name='crawl_url',
            field=models.URLField(verbose_name='Crawl URL'),
        ),
    ]
