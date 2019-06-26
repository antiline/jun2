from django.core.management import call_command
from uwsgidecorators import cron

from infras.constants.lock_constants import FileLockKeyName
from libs.lock.decorators import f_lock


@cron(0, -1, -1, -1, -1)
@f_lock(FileLockKeyName.CRAWL_GPX)
def check(signum: int):
    call_command('crawl_gpx')
