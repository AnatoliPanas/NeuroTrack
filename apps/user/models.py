from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Stages(models.TextChoices):
    EARLY_STAGE = 'early_stage', 'Early Stage'
    SCHOOL_STAGE = 'school_stage', 'School Stage'
    TEEN_STAGE = 'teen_stage', 'Adolescence & Adulthood'

class Doctor(User):
    name = models.CharField(max_length=20)
    nachname = models.CharField(max_length=20)
    specification = models.CharField(max_length=125)
    work_experience = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}.{self.nachname}'


class Group(models.Model):
    name = models.CharField(max_length=20)
    doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.SET_NULL, related_name='group')

    def __str__(self):
        return self.name


class Patient(models.Model):
    photo = models.CharField(max_length=255, null=True, blank=True)
    login = models.CharField(
        max_length=80,
        unique=True,
        help_text="Anstelle einer E-Mail-Adresse. Benutzerdefinierter Superheldenname."
    )
    image_password = models.CharField(max_length=255)
    restore_notification = models.BooleanField(default=False)
    doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.SET_NULL, related_name='patienten')

    age = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(3), MaxValueValidator(99)],
        verbose_name="Alter",
        help_text="Alter des Patienten (optional, 3-99 Jahre)",
    )
    adhd_stage = models.CharField(
        max_length=20,
        choices=Stages.choices,
        default=Stages.EARLY_STAGE
    )
    def __str__(self):
        return self.login
