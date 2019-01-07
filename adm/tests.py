from django.test import *
from django.shortcuts import render 

def index():
    return render(request, 'index.html')

# Create your tests here.
