# INF601 - Advanced Programming in Python
# Jackson Reed
# Mini Project 4

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('submit-form/', views.form_submit, name='form_submit'),
    path('view-forms/', views.view_submitted_forms, name='view_forms'),
    path('login-required/', views.login_required_view, name='login_required'),
]
