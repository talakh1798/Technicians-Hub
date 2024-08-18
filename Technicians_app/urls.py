
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome,name="welcome"),
    path('contact',views.contact,name='contact'),  
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('signin/', views.sign_in, name='signin'),

]

