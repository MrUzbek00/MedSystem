from django.urls import path
from .views import add_department,add_ward,add_appointment,settings,add_patient_to_ward,add_note,add_file,generate_report

app_name = 'ut'
urlpatterns = [
    path('add_department/',add_department,name="add_department"),
    path('add_ward/',add_ward,name="add_ward"),
    path('add_appointment/',add_appointment,name="add_appointment"),
    path('settings/',settings,name="settings"),
    path('register_ward/',add_patient_to_ward,name="register_patient"),
    path('add_note/',add_note,name="add_note"),
    path('add_file/',add_file,name="add_file"),
    path('generate_report/',generate_report,name="generate_report"),
]