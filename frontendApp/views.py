from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from backendApp.models import CustomUserModel,TravelerProfileModel


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')
def contact(request):
    return render(request, 'contact.html')
def packages(request):
    return render(request, 'package.html')
def team(request):
    return render(request, 'team.html')
def testimonials(request):
    return render(request, 'testimonial.html')
def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def become_guide(request):
    return render(request, 'become_guide.html')
def frontend_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUserModel.objects.get(email=email)
        except CustomUserModel.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect('frontend_login')

        # Only allow Traveler and Tour Guide
        if user.user_type not in ['traveler', 'tourguide']:
            messages.error(request, "Admin users cannot login here")
            return redirect('frontend_login')

        user_auth = authenticate(request, username=user.username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('index')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('frontend_login')

    return render(request, 'login.html')

def frontend_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('frontend_signup')


        if CustomUserModel.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please use a different email.")
            return redirect('frontend_signup')

        # Create new user
        user = CustomUserModel(username=email, email=email, first_name=first_name, last_name=last_name, user_type='traveler')
        user.set_password(password)
        user.save()
        TravelerProfileModel.objects.create(
            user_id=user,
            email=email,
            full_name=f"{first_name} {last_name}",
        )
        messages.success(request, "Account created successfully! Please login.")
        return redirect('frontend_login')

    return render(request, 'signup.html')
