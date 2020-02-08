"""
WSGI config for django_mlds project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys
sys.path.append("/home/deploy/apps/mlds/current")
sys.path.append("/var/www/html/django_mlds")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_mlds.settings_overrides.settings')


application = get_wsgi_application()
