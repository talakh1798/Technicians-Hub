from django.db import models
import bcrypt
import re
from datetime import datetime


class UserManager(models.Manager):
    def validate_registration(self,postData):
        errors = {}
        #validate the first name
        if len(postData['first_name']) < 2 :
            errors['first_name'] ='First  name must be at least 2 characters'
        #validate the last name
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be at least 2 characters'
            #validate the email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if User.objects.filter(email=postData['email']).exists():
            errors['email'] = "Email already in use!"
        #validate date of birthday
        if not postData['date_of_birth']:
            errors['date_of_birth'] = 'Date Of Birth is Mandatory'
        else:
            birthday = datetime.strptime(postData['date_of_birth'], "%Y-%m-%d").date()
            today = datetime.now().date()
            age = today.year - birthday.year
            if age < 18:
                errors["date_of_birth"] = "Age must be at least 18 years old"

        #validate the password

        if len(postData['password']) < 6:
            errors['password'] = 'Password must be at least 6 characters'
        # if len(postData['password']) != len(postData['confirm_password']):
        #     errors['password'] = 'Password do not match'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'Passwords do not match'

        return errors

#update class user
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()



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


def create_user(POST):
    password = POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    return User.objects.create(first_name = POST['first_name'],
                               last_name=POST['last_name'],
                               phone_number=POST['phone_number'],
                               date_of_birth = POST['date_of_birth'],
                               email = POST['email'],
                               password= pw_hash
                               )

def filter_email(POST):
    return User.objects.filter(email = POST['email'])