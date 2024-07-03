# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('user_home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']  # Use square brackets
        password = request.POST['password']  # Use square brackets
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def welcome(request):
    if request.method == 'GET':
        return render(request, 'welcome.html')
    
def user_home(request):
    if request.method == 'GET':
        user = request.user
        return render(request, 'home.html', {'user': user})
    

def upload_photos(request):
    if request.method == 'GET':
        user = request.user
        return redirect(reverse('upload_photo'))