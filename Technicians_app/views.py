from django.shortcuts import render,redirect
from .models import *
import bcrypt
from . import models
from django.contrib import messages

def welcome(request):
    return render(request, 'welcome.html')

def contact(request):
    return render(request, 'contact.html')

# this function attempts to authenticate the user by checking the provided email and password against the database. 
# If authentication is successful, it stores the user's ID and name in the session and redirects to the home page 
def login(request):
    if request.method == "POST" :
        email=request.POST['email']
        password=request.POST['password']
        user = User.objects.filter(email=email).first()
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if user and bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect('/')   
    return render(request, 'login.html', {'error': 'Invalid email or password'})
      
# this function renders the sign up page with a form for the user to input their information
def sign_up(request):
    if request.method == "POST" : 
        errors = User.objects.validate_registration(request.POST)
        if len(errors) > 0:
            # for key, value in errors.items():
            #     messages.error(request, value)
            return render(request, 'sign_up.html', {'errors': errors, 'data': request.POST})
        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()  # create the hash    
            print(pw_hash)
            user=models.create_account(request.POST,pw_hash=pw_hash)
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect('login')
    return render(request, 'sign_up.html',)

def about_us(request):
    return render(request, 'about_us.html')
