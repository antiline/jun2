import gpxpy
import gpxpy.gpx
import requests

from apps.domains.location.models.models import GpxCrawlStatus
from apps.domains.location.models.repositories import GpxCrawlStatusRepository, GpxPointRepository


class GpxCrawlService:
    @classmethod
    def crawl_all(cls):
        gpx_crawl_status_list = GpxCrawlStatusRepository.find_avail_all()
        for gpx_crawl_status in gpx_crawl_status_list:
            # TODO: Need exception handling to run continue.
            cls.crawl(gpx_crawl_status)

    @classmethod
    def crawl(cls, gpx_crawl_status: GpxCrawlStatus):
        user = gpx_crawl_status.user
        gpx = gpxpy.parse(cls._get_gpx_data(gpx_crawl_status.crawl_url))

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    gpx, created = GpxPointRepository.get_or_create(user=user, record_time=point.time, defaults={
                        'latitude': point.latitude,
                        'longitude': point.longitude,
                        'elevation': point.elevation,
                    }, )

                    if created:
                        continue

                    if gpx.change(point.latitude, point.longitude, point.elevation):
                        gpx.save()

    @classmethod
    def _get_gpx_data(cls, url) -> str:
        response = requests.get(url)
        return response.text
