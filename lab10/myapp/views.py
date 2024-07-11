from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    a=5
    return HttpResponse("This is a website for Django!!!!!!!!")
