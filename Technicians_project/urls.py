"""Technicians_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
=======
    path('admin/', admin.site.urls), #url admin
>>>>>>> 4dfe2c902f53ebca36f9c5c28573a442cf6f6541
    path('', include('Technicians_app.urls')),  # Add this line
]
