# Add Production Settings here
from .settings import *

DJANGO_ENV = "prod"

DEBUG = True
ALLOWED_HOSTS = ['mlds.korexindo.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mlds',                      # Or path to database file if using sqlite3.
        'USER': 'mldraft',                      # Not used with sqlite3.
        'PASSWORD': 'yriy0WR9LAgxXV',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# End with a Blank Line !
