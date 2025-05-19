import os
import django

from apps.user.models import Doctor

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from apps.user.models import Doctor



doc = Doctor(
name = 'Victor',
nachname = 'Abrams',
_username = 'v.abrams',
email = 'v.abrams@icloud.com',
specification = 'Psychologist-therapist',
work_experience = '15 years'
)

doc.set_password('a0fg785a979j132oh')
doc.save()