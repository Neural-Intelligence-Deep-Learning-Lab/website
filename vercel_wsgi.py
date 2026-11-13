# vercel_wsgi.py
import os
import sys

# Put the Django project dir (the one with manage.py) first on the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()