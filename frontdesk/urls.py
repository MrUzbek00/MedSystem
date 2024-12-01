from django.urls import path
from .views import dashboard,doctors,new_appointment,register_to_ward,appaintments,add_department,add_doctor,add_patient,ward_patients,wards,patients

app_name = 'fr'

urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('register_to_ward/',register_to_ward,name='register_to_ward'),
    path('doctors/',doctors,name='doctors'),
    path('new_appointment/',new_appointment,name='new_appointment'),
    path('appaintments/',appaintments,name='appaintments'),
    path('add_department/',add_department,name='add_department'),
    path('add_doctor/',add_doctor,name='add_doctor'),
    path('add_patient/',add_patient,name='add_patient'),
    path('ward_patients/',ward_patients,name='ward_patients'),
    path('wards/',wards,name='wards'),
    path('patients/',patients,name='patients'),
]