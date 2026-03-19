"""
ASGI config for job project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import sys

from django.core.asgi import get_asgi_application

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'apps')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

application = get_asgi_application()
