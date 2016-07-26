"""
WSGI config for renren_new project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os


PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.insert(0,PROJECT_DIR)


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "renren_new.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "renren_new.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()