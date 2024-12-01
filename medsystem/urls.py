"""
URL configuration for medsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .view import redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',redirect_view,name='home_page'),
    path('frontdesk/', include('frontdesk.urls')),
    path('accauntant/', include('accauntant.urls')),
    path('cashier/', include('cashier.urls')),
    path('client/', include('client.urls')),
    path('director/', include('director.urls')),
    path('doctor/', include('doctor.urls')),
    path('utils/', include('utils.urls')),
    path('user/', include('user.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


