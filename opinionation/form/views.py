# INF601 - Advanced Programming in Python
# Jackson Reed
# Mini Project 4

from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'templates/registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'templates/registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')
def home(request):
    return render(request, 'templates/form/home.html')

def about(request):
    return render(request, 'templates/form/about.html')

def form(request):
    return render(request, 'templates/form/form.html')