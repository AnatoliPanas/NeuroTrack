import os
import django



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from apps.user.models import Doctor


# doctor = Doctor.objects.create(
# name='Victor',
# username='Victor1',
# nachname='Abrams',
# email='v.abrams@icloud.com',
# password='a0fg785a979j132oh1',
# specification='Psychologist-therapist1',
# work_experience='151 years'
# )

doctor = Doctor(
name='Victor',
username='Victor2',
nachname='Abrams',
email='v.abrams@icloud.com',
specification='Psychologist-therapist1',
work_experience='151 years'
)

doctor.set_password('a0fg785a979j132oh1')

doctor.save()