from django.contrib import admin
from .models import Service,Specialization,Department,Appointment,PatientFiles


admin.site.register(Service)
admin.site.register(Specialization)
admin.site.register(Department)
admin.site.register(Appointment)
admin.site.register(PatientFiles)
# Register your models here.
