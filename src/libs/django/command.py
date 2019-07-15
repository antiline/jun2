import time

from django.core.management.base import BaseCommand
from django.db import close_old_connections

from libs.log.logger import logger


class CommonBaseCommand(BaseCommand):
    title = 'No title'

    @staticmethod
    def log_error(msg: str) -> None:
        logger.error(msg)

    @staticmethod
    def log_info(msg: str) -> None:
        logger.info(msg)

    def handle(self, *args, **options) -> None:
        start_time = time.clock()
        self.log_info('Command Start.')

        close_old_connections()
        self.run(*args, **options)
        close_old_connections()

        time_taken = time.clock() - start_time
        self.log_info('Command Done.  Time Taken : ' + str(round(time_taken, 1)))

    def run(self, *args, **options) -> None:
        raise NotImplementedError
