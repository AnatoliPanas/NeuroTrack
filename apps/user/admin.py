from django.contrib import admin

from apps.user.models import Doctor, Patient


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'nachname',
        'email',
        'specification',
        'work_experience',
        'last_login',
    ]
    search_fields = ['email',]
    list_filter = ['specification',  'work_experience',]

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'login',
        'restore_notification',
        'age',
        'adhd_stage',
        'doctor__nachname',

    ]
    search_fields = ['login', ]
    list_filter = ['adhd_stage', 'age', 'doctor__nachname', 'doctor__email']