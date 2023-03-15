from .base import *

ALLOWED_HOSTS = [env('ALLOWED_HOSTS_PROD')]
STATICFILES_DIRS = []
DEBUG = False

# DATABASES = {
#     "default": {
#         "ENGINE": 'django.db.backends.postgresql_psycopg2',
#         'NAME': env('DB_NAME'),
#         'USER': env('DB_USER'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': env('DB_HOST'),
#         'PORT': '5432',
#     }
# }