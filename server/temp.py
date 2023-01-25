import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
import django
django.setup()
from api.models import *

m = list(Book.objects.all())
print(m)