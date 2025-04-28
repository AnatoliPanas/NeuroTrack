import os
import django



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from apps.user.models import Doctor


doctor = Doctor.objects.create(
name='Victor',
nachname='Abrams',
email='v.abrams@icloud.com',
password='a0fg785a979j132oh',
specification='Psychologist-therapist',
work_experience='15 years'
)