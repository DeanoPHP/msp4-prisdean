from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
