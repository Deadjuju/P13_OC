import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
)
# reading .env file
environ.Env.read_env()


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

SENTRY_DSN = env('SENTRY_DSN')
DEBUG = env('DEBUG')

ALLOWED_HOSTS += ["oc-p13.herokuapp.com"]


# Inser whitenoise midlleware in MIDDLEWARE LIST
# in line after 'django.middleware.security.SecurityMiddleware'
index_SecurityMiddleware = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware')
whitenoise_middleware = 'whitenoise.middleware.WhiteNoiseMiddleware'
MIDDLEWARE.insert((index_SecurityMiddleware + 1), whitenoise_middleware)


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
