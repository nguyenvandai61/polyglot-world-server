"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from app.cloudinary_loader import CloudinaryLoader


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

CloudinaryLoader()
application = get_wsgi_application()
