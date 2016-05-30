#for deployment to openshift
import datetime
from django.shortcuts import render
from django.contrib import messages
from forms import *
from models import *

def index(request):
    return store_totals(request, region=None)

def store_totals(request, region=None):
    stores = []

    if region is None:
        region='Central'    
    locations = Location.objects.filter(region__name=region)
    for ltn in locations:
        for shop in Store.objects.filter(store_location__name=ltn):
            stores.append(shop)
    
    context = {
        'stores':stores,
        'region':region, 
    }
    return render(request, 'store_totals.html', context)

def store_profile(request, region=None, store_id=None):
    stock = Stock.objects.filter(store__id=store_id)            
    store_obj = Store.objects.filter(id=store_id)

    context = {
        'stock':stock,
        'store_obj':store_obj
    }
    return render(request, 'store_profile.html', context)

def location_stores(request, region=None, location_name=None):
    stores = Sto.objects.filter(store__id=store_id)            
    store_obj = Store.objects.filter(id=store_id)

    context = {
        'stock':stock,
        'store_obj':store_obj
    }
    return render(request, 'store_profile.html', context)        

def agent_profile(request, agent=None):
    agent_obj = Agent.objects.filter(username=agent)
    agent_stores = Store.objects.filter(agent__username=agent)

    context = {
        'agent_obj':agent_obj,
        'agent_stores':agent_stores
    }
    return render(request, 'agent_profile.html', context)

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

def products(request, prod_id=None):
    if not product_id is None:
        products = Products.objects.all()
    else:
        products = Products.objects.filter(product_id=prod_id)
        
    context = {
        'products':products
    }
    
    return render(request, 'products.html', context)