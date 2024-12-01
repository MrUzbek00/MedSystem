from django.urls import path
from .views import register_user,_login,_logout,register

app_name = 'user'

urlpatterns = [
    path('register_user/',register_user,name='register_user'),
    path('register/',register,name='register'),
    path('login/',_login,name='login'),
    path('logout/',_logout,name='logout')
]