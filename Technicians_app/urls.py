
from django.urls import path
from . import views

urlpatterns = [
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
    path('recent_reviews/', views.recent_reviews, name='recent_reviews'),
    path('logout/', views.logout_user, name='logout_user'),
    path('about_us', views.about_us,name="about_us"),
    path('services', views.services,name='services' ),
]


