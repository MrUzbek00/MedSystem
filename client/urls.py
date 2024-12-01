from django.urls import path
from .views import dashboard,client_details,doctors,new_appointment,make_payment,update_profile

app_name = 'cl'

urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('client_details/',client_details,name='client_details'),
    path('doctors/',doctors,name='doctors'),
    path('new_appointment/',new_appointment,name='new_appointment'),
    path('new_appointment/<int:doctor_id>/',new_appointment,name='new_appointment'),
    path('make_payment/<int:id>/',make_payment,name='make_payment'),
    path('update_profile/',update_profile,name='update_profile'),
]