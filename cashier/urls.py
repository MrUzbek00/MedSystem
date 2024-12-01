from django.urls import path
from .views import dashboard,invoice,generate_report

app_name = 'ca'

urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('passed_invoice/<int:id>/',invoice,name='passed_invoice'),
    path('generate_report/',generate_report,name='generate_report'),
]