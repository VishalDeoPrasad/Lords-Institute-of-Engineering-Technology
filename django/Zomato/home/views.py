from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is my 🏠Home Page:")

def login(request):
    return HttpResponse("This is my 🗝️login page:")

def register(request):
    return HttpResponse("This is my 👤Register Page:")

def aboutus(request):
    return HttpResponse("This is my 🌟About us page")