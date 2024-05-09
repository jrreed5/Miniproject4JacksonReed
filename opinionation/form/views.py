# INF601 - Advanced Programming in Python
# Jackson Reed
# Mini Project 4

from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
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
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def form_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        submitted_form = SubmittedForm(name=name, email=email, message=message)
        submitted_form.save()

        return render(request, 'form/form_submit_success.html')
    else:
        return login_required_view(request)


@login_required
def view_submitted_forms(request):
    # logic to retrieve and display submitted forms
    forms = SubmittedForm.objects.all()
    return render(request, 'form/view_forms.html', {'forms': forms})

def login_required_view(request):
    return render(request, 'registration/login_required.html')

def user_logout(request):
    logout(request)
    return redirect('home')
def home(request):
    return render(request, 'form/home.html')

def about(request):
    return render(request, 'form/about.html')

def form(request):
    return render(request, 'form/form_submit.html')