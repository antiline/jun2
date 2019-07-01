from django.core.management import call_command
from uwsgidecorators import cron

from infras.constants.lock_constants import FileLockKeyName
from libs.lock.decorators import f_lock


@cron(-5, -1, -1, -1, -1)
@f_lock(FileLockKeyName.CRAWL_GPX, lock_ttl=3600*24)
def crawl_gpx(signum: int):
    call_command('crawl_gpx')
