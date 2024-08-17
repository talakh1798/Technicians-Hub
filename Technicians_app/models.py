from django.db import models

<<<<<<< Updated upstream
# Create your models here.
=======
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

class Technician(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    bio = models.TextField()
    phone_number = models.CharField(max_length=25)
    city = models.CharField(max_length=45)
    age = models.IntegerField()
    image = models.ImageField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    users = models.ManyToManyField(User, related_name="technicians")

#update class review
class Review(models.Model):
    technician = models.ForeignKey(Technician, related_name= "technician_reviews",  on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, related_name= "user_reviews", on_delete=models.CASCADE, default=1)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



>>>>>>> Stashed changes
