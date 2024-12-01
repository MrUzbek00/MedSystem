from django.urls import path
from .views import dashboard,paid_invoice

app_name = 'ac'

urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('passed_invoice/<int:id>/',paid_invoice,name='passed_invoice'),
]