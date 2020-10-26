from hello.views import fybsc, signup
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("login", views.login, name='Login'),
    path("signup", views.signup, name='Signup'),
    path("forgetpassword", views.forgetpassword, name='Password'),
    path("fybsc", views.fybsc, name = 'FYBSC'),
    path("sybsc", views.sybsc, name = 'SYBSC'),
    path("notice", views.notice, name = 'Notice')
]