from hello.views import fybsc, handlelogout, result, search, signup
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("login", views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name = 'handlelogout'),
    path("signup", views.signup, name='Signup'),
    path("forgetpassword", views.forgetpassword, name='Password'),
    path('result', views.result, name="result"),
    path("fybsc", views.fybsc, name = 'FYBSC'),
    path("sybsc", views.sybsc, name = 'SYBSC'),
    path("notice", views.notice, name = 'Notice'),
    path("search", views.search, name = "search")
]