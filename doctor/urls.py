from django.urls import path
from .views import dashboard,head_dashboard,ward_patient,patient_details,doctors,appointments

app_name = 'doc'

urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('dashboard/<int:doc_id>/',dashboard,name='v1dashboard'),
    path('doctors/',doctors,name='doctors'),
    path('appointments/',appointments,name='appointments'),
    path('head_dashboard/',head_dashboard,name='head_dashboard'),
    path('ward_patient/',ward_patient,name='ward_patient'),
    path('patient_details/<int:id>/',patient_details,name='patient_details'),
]