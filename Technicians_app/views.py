from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
import bcrypt
from . import models
from django.contrib import messages
from django.contrib.auth import logout
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail

def welcome(request):
    return render(request, 'welcome.html')

def contact(request):
    return render(request, 'contact.html')

def add_contact(request):
    if request.method == 'POST':
        contact = create_contact(request.POST)
        send_confirmation_email(contact)
        return redirect('/contact')
    return render(request, 'contact.html')


def send_confirmation_email(contact):
    subject = 'We Have Received Your Contact Request'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [contact.email]

    email_body = (
        f"Dear {contact.name},\n\n"
        "Thank you for reaching out to us. We have received your message and our team will "
        "get in touch with you shortly. We appreciate your patience and look forward to assisting you.\n\n"
        "Best regards,\n"
        "The TechHub Team\n"
    )

    email = EmailMessage(
        subject=subject,
        body=email_body,
        from_email=from_email,
        to=recipient_list
    )
    email.send()



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

        # Check if the user has already reviewed this technician
        existing_review_instance = existing_review(request)
        if existing_review_instance:
            messages.error(request, "You have already reviewed this technician.", extra_tags='danger')
            return redirect('review_form', technician_id=technician_id)

        # If no existing review, add the new review
        add_review(request)
        technician = get_technician(technician_id)
        messages.success(request, f"Review submitted successfully for technician {technician.first_name} {technician.last_name}", extra_tags='success')

        # Render the review form again after submission
        return render(request, 'review_form.html', {'technician': technician, 'technician_id': technician_id})
    
    return redirect('/')

def review_form(request, technician_id):
    if 'id' not in request.session:
        return redirect('login')

    user_id = request.session['id']
    user = models.get_user(user_id)
    technician = models.get_technician(technician_id)

    return render(request, 'review_form.html', {'user': user, 'technician_id': technician_id, 'technician': technician})

def recent_reviews(request):
    if 'id' in request.session:
        user_id = request.session['id']
        user = models.get_user(user_id)
        user_reviews = models.get_reviews_by_user(user_id)  
        return render(request, 'recent_reviews.html', {'user': user, 'user_reviews': user_reviews})
    else:      
        return redirect('login')  

def update_review(request, review_id):
    if 'id' not in request.session:
        return redirect('login')

    user_id = request.session['id']
    review = models.get_review(review_id)
    
    if review.user_id != user_id:
        messages.error(request, "You are not authorized to update this review.")
        return redirect('/recent_reviews')

    technician = review.technician  

    if request.method == 'POST':
        models.update_review(request, review_id)
        messages.success(request, f"Review for technician {technician.first_name} {technician.last_name} updated successfully.", extra_tags='info')
        return redirect('/recent_reviews')
    else:
        return render(request, 'update_review.html', {'review': review, 'technician': technician})
    
def delete_review(request, review_id):
    if 'id' not in request.session:
        return redirect('login')

    user_id = request.session['id']
    review = models.get_review(review_id)

    
    if review.user_id != user_id:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect('/recent_reviews')

    technician = review.technician
    models.delete_review(review_id)
    messages.success(request, f"Review for technician {technician.first_name} {technician.last_name} deleted successfully.", extra_tags='success')
    return redirect('/recent_reviews')

def logout_user(request):
    logout(request)
    return redirect('/')

def services(request):

    roles = Role.objects.all()
    context = {
        'roles': roles,
        'current_year': datetime.now().year,
    }
    return render(request, 'services.html',context)

def role_detail(request, id):
    try:
        role = Role.objects.get(id=id)
        technicians = Technician.objects.filter(role=role)
    except Role.DoesNotExist:
        role = None
        technicians = []

    context = {
        'role': role,
        'technicians': technicians,
        'current_year': datetime.now().year
    }
    return render(request, 'technicians.html', context)

def terms(request):
    return render(request, 'terms_of_use.html')

def privacy_policy(request):
    return render (request, 'privacy_policy.html')
   
def book_technician(request, technician_id):
    try:
        technician = Technician.objects.get(id=technician_id)
    except Technician.DoesNotExist:
        return render(request, 'technician_not_found.html')

    if request.method == 'POST':
        user = request.user 
        return redirect('confirm_booking', technician_id=technician.id)
    return render(request, 'book.html', {'technician': technician})


def confirm_booking(request, technician_id):
    try:
        technician = Technician.objects.get(id=technician_id)
    except Technician.DoesNotExist:
        return redirect('technicians')  # Redirect if technician is not found
    if request.method == 'POST':
        context = {
            'technician': technician
        }
        return render(request, 'confirm_booking.html', context)
    else:
        return redirect('technicians')


def book_appointment(request, technician_id):
    technician = models.get_technician(technician_id)
    if request.method == 'POST':
        request.session['technicianid'] = technician_id
        appointment = models.add_appointment(request)
        send_mail(
            'Appointment Booked Successfully',
            f'Your Appointment with techncian {technician.first_name} {technician.last_name} has been booked on {appointment.date} at {appointment.time}.',
            'izzidinsamara@gmail.com',
            [appointment.user.email],
            fail_silently=False,
        )
        technician = get_technician(technician_id)
        messages.success(request, f"Appointment booked successfully  with  technician {technician.first_name} {technician.last_name}", extra_tags='success')
        # Render the review form again after submission
        return render(request, 'appointment_form.html', {'technician': technician, 'technician_id': technician_id})
    
    return redirect('/')

def appointment_form(request, technician_id):
    if 'id' not in request.session:
        return redirect('login')
    user_id = request.session['id']
    user = models.get_user(user_id)
    technician = models.get_technician(technician_id)
    return render(request, 'appointment_form.html', {'user': user, 'technician_id': technician_id, 'technician': technician})