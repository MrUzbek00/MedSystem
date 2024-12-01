from django.contrib import admin
from .models import CustomUser,Admin,Frontdesk,Doctor,Cashier,Patient,Accauntant,Director

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Frontdesk)
admin.site.register(Doctor)
admin.site.register(Director)
admin.site.register(Cashier)
admin.site.register(Patient)
admin.site.register(Accauntant)