from apps.domains.location.services.gpx_crawl_service import GpxCrawlService
from libs.django.command import CommonBaseCommand


class Command(CommonBaseCommand):
    title = 'Crawl gpx'
    help = 'Crawl gpx'

    def run(self, *args, **options):
        GpxCrawlService.crawl_all()
