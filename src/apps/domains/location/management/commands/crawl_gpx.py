from apps.domains.location.services.gpx_crawl_service import GpxCrawlService
from libs.django.command import CommonBaseCommand


class Command(CommonBaseCommand):
    title = 'check operation queue'
    help = 'check operation queue'

    def run(self, *args, **options):
        GpxCrawlService.crawl_all()
