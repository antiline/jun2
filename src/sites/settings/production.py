# noinspection PyUnresolvedReferences
from .base import *  # flake8: noqa: F403  # pylint:disable=wildcard-import
from libs.log.setup import setup_logging

DEBUG = False

setup_logging(DEBUG)

ALLOWED_HOSTS = ['127.0.0.1', ]
