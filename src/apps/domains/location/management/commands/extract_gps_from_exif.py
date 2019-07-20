from apps.domains.location.services.extract_gps_from_exif_service import ExtractGpsFromExifService
from libs.django.command import CommonBaseCommand


class Command(CommonBaseCommand):
    title = 'Extract gps on exif'
    help = 'Extract gps on exif'

    def run(self, *args, **options):
        ExtractGpsFromExifService.extract_all()
