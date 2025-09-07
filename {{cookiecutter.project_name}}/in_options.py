
import json
import os
from typing import Counter
import django
import sys
from pathlib import Path
from django.contrib.auth.hashers import make_password
 

base_dir = str(Path(__file__).resolve().parent)
if base_dir.lower() not in sys.path:
    sys.path.append(base_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{{cookiecutter.project_name}}.settings")
django.setup()

from django.db.models import Q

if __name__ == "__main__":#
    pass