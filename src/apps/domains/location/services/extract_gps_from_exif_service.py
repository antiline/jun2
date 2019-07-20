import os

from django.contrib.auth.models import User

from apps.domains.location.helpers.exif_helper import ExifHelper, ExifParseException
from apps.domains.location.models.models import ExtractGpsFromExifStatus
from apps.domains.location.models.repositories import ExtractGpsFromExifStatusRepository, GpxPointRepository


class ExtractGpsFromExifService:
    ALLOW_EXTENSIONS = ['.jpg']

    @classmethod
    def extract_all(cls):
        status_list = ExtractGpsFromExifStatusRepository.find_avail_all()
        for status in status_list:
            cls.extract_by_status(status)

    @classmethod
    def extract_by_status(cls, status: ExtractGpsFromExifStatus):
        for (path, _, filenames) in os.walk(status.image_path):
            for filename in filenames:
                ext = os.path.splitext(filename)[1]
                if ext.lower() not in cls.ALLOW_EXTENSIONS:
                    continue

                cls.extract_from_file(status.user, os.path.join(path, filename))

    @classmethod
    def extract_from_file(cls, user: User, filepath: str):
        try:
            gps_datetime, latitude, longitude, altitude, = ExifHelper.parse_gps_data(filepath)
        except ExifParseException:
            return

        GpxPointRepository.update_or_create(user=user, record_time=gps_datetime, defaults={
            'latitude': latitude,
            'longitude': longitude,
            'elevation': altitude,
        }, )
