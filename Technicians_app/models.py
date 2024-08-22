from django.db import models
import bcrypt
import re
from datetime import datetime
from django.shortcuts import get_object_or_404


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
        # Add a password and validate that password at least 8 characters
        if len(postData['password']) < 6:
            errors['password'] = 'Password must be at least 6 characters'
        # if len(postData['password']) != len(postData['confirm_password']):
        #     errors['password'] = 'Password do not match'
        if postData['password'] != postData['confirm_password']:
            errors['password_match'] = 'Passwords do not match'

        # Add a phone number and validate that the user's number should be at least 10 digits
        if len(postData['phone_number']) < 10:
            errors['phone_number'] = "Phone number should be at least 10 digits long."

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

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.CharField(max_length=255)

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


def create_account(request,pw_hash):
    first_name=request['first_name']
    last_name=request['last_name']
    email=request['email']
    password=pw_hash
    date_of_birth=request['date_of_birth']
    phone_number=request['phone_number']
    return User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, date_of_birth=date_of_birth, phone_number=phone_number)

def create_contact(POST):
    return Contact.objects.create(
        name = POST['name'],email = POST['email'],message=['message']

    )

def filter_email(POST):
    return User.objects.filter(email = POST['email'])

def add_review(request):
    user_id = request.session['userid']
    technician_id = request.session['technicianid']
    content = request.POST['content']
    user = get_object_or_404(User, id=user_id)
    technician = get_object_or_404(Technician, id=technician_id)
    review = Review.objects.create(content=content, user=user, technician=technician)
    return review

def existing_review(request):
    user_id = request.session['userid']
    technician_id = request.session['technicianid']
    user = get_object_or_404(User, id=user_id)
    technician = get_object_or_404(Technician, id=technician_id)
    return Review.objects.filter(technician=technician, user=user).first()

def get_technician(technician_id):
    return get_object_or_404(Technician, id=technician_id)

def get_review(review_id):
    review = get_object_or_404(Review, id=review_id)
    return review

def update_review(request, review_id): 
    review = get_object_or_404(Review, id=review_id)
    review.content = request.POST['content']
    review.save()

def delete_review(review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return review

def show_all_reviews():
    return Review.objects.all()

def get_user(user_id):
    user = get_object_or_404(User, id=user_id)
    return user

def get_reviews_by_user(user_id):
    return Review.objects.filter(user__id=user_id)

