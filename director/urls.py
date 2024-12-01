from django.urls import path
from .views import dashboard,staticsts

app_name = 'dr'

urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('staticsts/',staticsts,name='staticsts'),
]