from django.db import models

# 
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Technicians(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    bio = models.TextField()
    phone_number = models.CharField(max_length=25)
    city = models.CharField(max_length=45)
    age = models.IntegerField()
    image = models.ImageField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    