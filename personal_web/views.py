from django.shortcuts import render
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def projects(request):
    return render(request, 'projects.html')

def publications(request):
    return render(request, 'publications.html')

def contact(request):
    return render(request, 'contact.html')

def teaching(request):
    return render(request, 'teaching.html')

def awards(request):
    return render(request, 'awards.html')


