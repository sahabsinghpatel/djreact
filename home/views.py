from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def services(request):
    return render(request, 'home/services.html')

def contact(request):
    return render(request, 'home/aboutcontact.html')
