
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome,name="welcome"),  # Add this line
    path('contact',views.contact,name='contact'),  
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('signin/', views.sign_in, name='signin'),
    path('about_us/', views.about_us,name="about_us"),
]

