from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def bookstore(request):
    return render(request, 'base.html')
