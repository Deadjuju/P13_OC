from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS += ["oc-p13.herokuapp.com"]


# Inser whitenoise midlleware in MIDDLEWARE LIST 
# in line after 'django.middleware.security.SecurityMiddleware'
index_SecurityMiddleware = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware')
whitenoise_middleware = 'whitenoise.middleware.WhiteNoiseMiddleware'
MIDDLEWARE.insert((index_SecurityMiddleware + 1), whitenoise_middleware)


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
