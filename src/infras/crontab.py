from django.core.management import call_command
from uwsgidecorators import timer

from infras.constants.lock_constants import FileLockKeyName
from libs.lock.decorators import f_lock


@timer(10)
@f_lock(FileLockKeyName.SYSTEM_CHECK)
def check(signum: int):
    call_command('check')
