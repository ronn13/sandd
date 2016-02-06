#for deployment to openshift
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def agents(request):
    return render(request, 'agents.html')

def agent_form(request):
    return render(request, 'agent_form.html')

