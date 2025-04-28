from django.contrib import admin

from apps.user.models import Doctor


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
