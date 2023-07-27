from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def one(request):
    return render(request, 'index5.html')

def two(request):
    return render(request, 'index6.html')

def three(request):
    return HttpResponse('<center><h1>This is the string response of app3</h1></center>')