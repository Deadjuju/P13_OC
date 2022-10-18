import environ

from .base import *


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
)
# reading .env file
environ.Env.read_env()


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS += ["oc-p13.herokuapp.com"]


# Inser whitenoise midlleware in MIDDLEWARE LIST
# in line after 'django.middleware.security.SecurityMiddleware'
index_SecurityMiddleware = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware')
whitenoise_middleware = 'whitenoise.middleware.WhiteNoiseMiddleware'
MIDDLEWARE.insert((index_SecurityMiddleware + 1), whitenoise_middleware)


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
