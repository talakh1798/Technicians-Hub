
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome,name="welcome"),  # Add this line
    path('about_us/', views.about_us,name="about_us"),
]
