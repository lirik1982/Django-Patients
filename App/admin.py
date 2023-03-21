from django.contrib import admin
from App.models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'gender', 'age', 'created_at']
    search_fields = ['name', 'phone', 'email', 'age']
    list_filter = ['gender']
    list_per_page = 2

admin.site.register(Patient, PatientAdmin)


