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

ALLOWED_HOSTS += ["127.0.0.1", "localhost"]
