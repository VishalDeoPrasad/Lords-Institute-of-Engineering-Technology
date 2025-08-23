from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to my 🏠Home Page!")

def login(request):
    return HttpResponse("Welcome to my 🗝️Login Page!")

def register(request):
    return HttpResponse("Welcome to my 👤Register Page!")