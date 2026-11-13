import os
import sys

# Add Django project directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), "main"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()