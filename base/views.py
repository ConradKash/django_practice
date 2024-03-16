from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home Page')

def login(request):
    return HttpResponse('Login Page')

def signup(request):
    return HttpResponse('Signup Page')

def logout(request):
    return HttpResponse('Logout Page')