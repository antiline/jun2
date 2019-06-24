import os

from django.core.wsgi import get_wsgi_application

from infras.secrets.constants import SecretKey
from libs.secrets.secrets import Secrets

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'sites.settings.{Secrets.get(SecretKey.ENVIRONMENT)}')

application = get_wsgi_application()
