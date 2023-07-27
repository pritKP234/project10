from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def one(request):
    return render(request, 'index1.html')

def two(request):
    return render(request, 'index2.html')

def three(request):
    return HttpResponse('<h1>This is the string response of app1</h1>')