from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def admission(request):
    return render(request, 'admission.html')

def campuslife(request):
    return render(request, 'campuslife.html')