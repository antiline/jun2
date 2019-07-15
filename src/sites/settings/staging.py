from libs.log.setup import setup_logging

# flake8: noqa: F403
# pylint:disable=wildcard-import, unused-wildcard-import
# noinspection PyUnresolvedReferences
from .base import *

DEBUG = False

setup_logging(DEBUG)

ALLOWED_HOSTS = ['127.0.0.1', ]
