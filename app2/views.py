from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def one(request):
    return render(request, 'index3.html')

def two(request):
    return render(request, 'index4.html')

def three(request):
    return HttpResponse('<center><h1>This is the string response of app2</h1></center>')