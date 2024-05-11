# INF601 - Advanced Programming in Python
# Jackson Reed
# Mini Project 4

from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import SubmittedFormData


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

        submitted_form = SubmittedFormData(name=name, email=email, message=message)
        submitted_form.save()

        return render(request, 'form/form_submit_success.html')
    else:
        return login_required_view(request)


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_message = "You have successfully logged in."

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect to home page if already logged in
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


@login_required
def view_submitted_forms(request):
    # logic to retrieve and display submitted forms
    forms = SubmittedFormData.objects.all()
    return render(request, 'form/view_forms.html', {'forms': forms})


def login_required_view(request):
    return render(request, 'registration/login_required.html')


def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')


def home(request):
    return render(request, 'form/home.html')


def about(request):
    return render(request, 'form/about.html')


def form(request):
    return render(request, 'form/form_submit.html')
