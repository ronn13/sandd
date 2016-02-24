#for deployment to openshift
from django.shortcuts import render
from django.contrib import messages
from forms import *
from models import *

def index(request):
    return render(request, 'index.html')

def agents(request):
    return render(request, 'agents.html')

def agent_form(request):
    store = Store.objects.all()
    if request.POST:
        form = ProductsForm(request.POST)
        if form.is_valid():
            store = form.cleaned_data['store']
            shampoo = form.cleaned_data['shampoo']
            hairgel = form.cleaned_data['hairgel']
            relaxer = form.cleaned_data['relaxer']
            stock_type = form.cleaned_data['stock_type']
            form.save()
            messages.add_message(request, messages.SUCCESS, "Stock updated for %s" % store)
            form = ProductsForm()                
    else:
        form = ProductsForm()
        
    return render(request, 'agent_form.html', locals())
