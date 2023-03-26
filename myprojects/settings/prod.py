from .base import *

ALLOWED_HOSTS = [env('ALLOWED_HOSTS_PROD'), '1mprojects.com']

#The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = (BASE_DIR / 'static')

STATICFILES_DIRS = []

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
}