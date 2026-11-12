import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1] / "main"
sys.path.insert(0, str(PROJECT_ROOT / "main"))
sys.path.insert(0, str(PROJECT_ROOT))

from wsgi import application

app = application
