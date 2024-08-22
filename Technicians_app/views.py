from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
import bcrypt
from . import models
from django.contrib import messages
from django.contrib.auth import logout

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
            return redirect('services')   
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

def create_review(request, technician_id):
    if request.method == 'POST':
        request.session['technicianid'] = technician_id
        
        
        existing_review_instance = models.existing_review(request)
        if existing_review_instance:
            messages.error(request, "You have already reviewed this technician.", extra_tags='danger')
            return redirect(f'/review_form/{technician_id}')
        
        
        models.add_review(request)
        technician = models.get_technician(technician_id)
        messages.success(request, f"Review submitted successfully for technician {technician.first_name} {technician.last_name}", extra_tags='success')
        return redirect('/recent_reviews')
    return redirect('/')

def review_form(request, technician_id):
    technician = models.get_technician(technician_id)
    return render(request, 'review_form.html', {'technician_id': technician_id, 'technician' : technician})

def recent_reviews(request):
    if 'userid' in request.session:
        user_id = request.session['userid']
        user = models.get_user(user_id)
        user_reviews = models.get_reviews_by_user(user_id)  
        return render(request, 'recent_reviews.html', {'user': user, 'user_reviews': user_reviews})
    else:      
        return redirect('login')  

def update_review(request, review_id):
    review = models.get_review(review_id)
    technician = review.technician  

    if request.method == 'POST':
        models.update_review(request, review_id)
        messages.success(request, f" Review for technician {technician.first_name} {technician.last_name} updated successfully.", extra_tags='info')
        return redirect('/recent_reviews')
    else:
        return render(request, 'update_review.html', {'review': review, 'technician': technician})
    
def delete_review(request, review_id):
    review = models.get_review(review_id)
    technician = review.technician
    models.delete_review(review_id)   
    messages.success(request, f" Review for technician {technician.first_name} {technician.last_name} deleted successfully.", extra_tags='success')
    return redirect('/recent_reviews', {'review' : review, 'technician' : technician})

def logout_user(request):
    logout(request)
    return redirect('/')

def services(request):
    return render(request, 'services.html')

