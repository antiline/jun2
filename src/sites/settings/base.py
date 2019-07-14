import logging
import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.excepthook import ExcepthookIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from infras.secrets.constants import SecretKey
from libs.secrets.secrets import Secrets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = Secrets.get(SecretKey.SECRET_KEY)

DEBUG = False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',

    # Apps
    'apps.domains.home.apps.HomeConfig',
    'apps.domains.location.apps.LocationConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'libs.django.admin.middlewares.AdminIPRestrictorMiddleware',
]

ROOT_URLCONF = 'sites.urls'
WSGI_APPLICATION = 'sites.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': Secrets.get(SecretKey.WRITE_DB_NAME),
        'USER': Secrets.get(SecretKey.WRITE_DB_USER),
        'PASSWORD': Secrets.get(SecretKey.WRITE_DB_PASSWORD),
        'HOST': Secrets.get(SecretKey.WRITE_DB_HOST),
        'PORT': Secrets.get(SecretKey.WRITE_DB_PORT),
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Security

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Admin

RESTRICT_ADMIN = True
ALLOWED_ADMIN_IPS = ['127.0.0.1', '::1']
ALLOWED_ADMIN_IP_RANGES = ['127.0.0.0/24', '192.168.0.0/16', '172.16.0.0/12', '::/1']
ALLOWED_ADMIN_PROXY_COUNT = 1
RESTRICTED_APP_NAMES = ['admin']

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/src', ),)
STATIC_ROOT = os.path.join(BASE_DIR, 'static/dist')

# Sentry

sentry_sdk.init(
    dsn=Secrets.get(SecretKey.SENTRY_DSN),
    integrations=[DjangoIntegration(), ExcepthookIntegration(always_run=True), LoggingIntegration(logging.INFO, logging.ERROR), ]
)
