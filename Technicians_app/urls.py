
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome,name="welcome"),  # Add this line
    path('contact',views.contact,name='contact'),  
    path('login', views.login,name='login'),
    path('sign_up', views.sign_up,name='sign_up'),
    path('about_us', views.about_us,name="about_us"),
]

