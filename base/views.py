from django.shortcuts import render
from django.http import HttpResponse

categories = [
    {'id': '1', 'Name': 'Admin'},
    {'id': '2', 'Name': 'Patient'},
    {'id': '3', 'Name': 'Pharmacy'},
    {'id': '4', 'Name': 'Doctor'},
]

# Create your views here.
def home(request):
    context = {'categories':categories}
    return render(request, 'base\home.html', context)

def login(request):
    return render(request, 'base\login.html')

def signup(request):
    return HttpResponse('Signup Page')

def logout(request):
    return HttpResponse('Logout Page')