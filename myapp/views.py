from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from.models import ContactMessage


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Account created successfully! Please login.')
                return redirect('login_view')
        else:
         messages.error(request, 'Passwords do not match')
    return render(request, 'register.html')

    


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login_view')


def home(request):
    return render(request,'home.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')
        message = request.POST.get('message', '')
        
        if name and email and phone_number and message:
            # Save the message to the database
            ContactMessage.objects.create(name=name, email=email, phone_number=phone_number, message=message)
            
            # Success message
            messages.success(request, "Your message has been sent successfully!")
            
            # Redirect to prevent re-posting the form data on refresh
            return redirect('contact')
        else:
            # Error message if any field is empty
            messages.error(request, "Please fill in all fields.")
    
    # Render the contact form
    return render(request, 'contact.html')

     