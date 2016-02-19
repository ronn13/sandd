#for deployment to openshift
from django.shortcuts import render
from forms import *

def index(request):
    return render(request, 'index.html')

def agents(request):
    return render(request, 'agents.html')

def agent_form(request):
    if request.POST:
        form = ProductsForm(request.POST)
        if form.is_valid():
            return render(request, 'agent_form.html')    
    else:
        return render(request, 'agent_form.html')

