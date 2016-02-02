#for deployment to openshift
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# Create your views here.
