
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.welcome,name="welcome"), 
    path('contact',views.contact,name='contact'),  
    path('login', views.login,name='login'),
    path('sign_up', views.sign_up,name='sign_up'),
    path('add_contact',views.add_contact,name = 'add_contact'),
    path('about_us/', views.about_us,name="about_us"),
    path('review_form/<int:technician_id>/', views.review_form, name='review_form'),
    path('create_review/<int:technician_id>/', views.create_review, name='create_review'),
    path('update_review/<int:review_id>/', views.update_review, name='update_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('recent_reviews', views.recent_reviews, name='recent_reviews'),
    path('logout/', views.logout_user, name='logout_user'),
    path('about_us', views.about_us,name="about_us"),
    path('services', views.services,name='services' ),
    path('role/<int:id>/', views.role_detail, name='role_detail'),
    path('terms',views.terms,name='terms'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'), 
    path('appointment_form/<int:technician_id>/', views.appointment_form, name='appointment_form'),
    path('book_appointment/<int:technician_id>/', views.book_appointment, name='book_appointment'),
    path('update_appointment/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('cancel_appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('recent_appointments', views.recent_appointments, name='recent_appointmens'),
    path('recent_reviews/confirm_delete/<int:review_id>/', views.confirm_delete_review, name='confirm_delete_review'),
    path('recent_appointments/confirm_cancel/<int:appointment_id>/', views.confirm_cancel_appointment, name='confirm_cancel_appointment'),
    path('accounts/profile/', views.profile_redirect, name='profile_redirect'),

]


