from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

def welcome(request):
    return render(request, 'welcome.html')

def signup(request):
    return render(request,'sign_up.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.validate_registration(request.POST)
        if errors:
            for error in errors.values():
                messages.error(request,error)
            return redirect('signup')
        #if there  is no error in the inputs, create a new user and save it in session
        user=create_user(request.POST)
        request.session['user_id'] = user.id
        return redirect('/')
    else:
        return redirect('/')
    
def sign_in(request):
    if request.method == 'POST':
        user = filter_email(request.POST)
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/')
            else:
                messages.error(request, 'invalid  password or email')
                return redirect('/login')
        
                
    
