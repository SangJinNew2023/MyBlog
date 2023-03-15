from .base import *

ALLOWED_HOSTS = [env('ALLOWED_HOSTS_PROD')]

#The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = (BASE_DIR / 'static')

STATICFILES_DIRS = []

DEBUG = False

