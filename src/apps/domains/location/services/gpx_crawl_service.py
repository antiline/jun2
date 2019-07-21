import gpxpy
import gpxpy.gpx
import requests
from requests import RequestException
from sentry_sdk import capture_message

from apps.domains.location.constants import GpxPointRefType
from apps.domains.location.models.models import GpxCrawlStatus
from apps.domains.location.models.repositories import GpxCrawlStatusRepository, GpxPointRepository
from libs.base.exceptions import NetworkException
from libs.decorators.retry import retry


class GpxCrawlService:
    @classmethod
    def crawl_all(cls):
        gpx_crawl_status_list = GpxCrawlStatusRepository.find_avail_all()
        for gpx_crawl_status in gpx_crawl_status_list:
            cls.crawl(gpx_crawl_status)

    @classmethod
    def crawl(cls, gpx_crawl_status: GpxCrawlStatus):
        user = gpx_crawl_status.user

        try:
            gpx = gpxpy.parse(cls._get_gpx_data(gpx_crawl_status.crawl_url))

        except (NetworkException, ValueError) as e:
            capture_message(e)
            return

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    gpx, created = GpxPointRepository.get_or_create(user=user, record_time=point.time, defaults={
                        'latitude': point.latitude,
                        'longitude': point.longitude,
                        'elevation': point.elevation,
                        'ref_type': GpxPointRefType.GPX
                    }, )

                    if created:
                        continue

                    if gpx.change(point.latitude, point.longitude, point.elevation, GpxPointRefType.GPX):
                        gpx.save()

    @classmethod
    @retry()
    def _get_gpx_data(cls, url) -> str:
        response = requests.get(url)

        try:
            response.raise_for_status()
        except RequestException as e:
            raise NetworkException from e

        return response.text
