# noinspection PyUnresolvedReferences
from .base import *  # flake8: noqa: F403  # pylint:disable=wildcard-import
from libs.log.setup import setup_logging

DEBUG = True

setup_logging(DEBUG)

ALLOWED_HOSTS = ['127.0.0.1', ]

# django-debug-toolbar
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": 'libs.django.utils.request.is_private_ip_from_request',
    'SHOW_COLLAPSED': True,
}

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
