import datetime
from urllib.parse import unquote

from django.shortcuts import render
from django.contrib import messages

from .forms import *
from .models import *

def index(request):
    return store_totals(request)

def store_totals(request, location=None):
    if location is None:
        stores = Store.objects.all()
    else:
        stores = Store.objects.filter(store_location__name=location)
    
    context = {
            'stores':stores, 
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
    stock = Stock.objects.filter(store__id=store_id)            
    store_obj = Store.objects.filter(id=store_id)

    context = {
        'stock':stock,
        'store_obj':store_obj
    }
    return render(request, 'store_profile.html', context)        

def agent_profile(request, agent=None):
    agent_obj = Agent.objects.filter(username__iexact=agent)
    agent_stores = Store.objects.filter(agent__username__iexact=agent)

    context = {
        'agent_obj':agent_obj,
        'agent_stores':agent_stores
    }
    return render(request, 'agent_profile.html', context)

def agent_form(request):
    store = Store.objects.all()
    if request.POST:
        form = StockForm(request.POST)
        if form.is_valid():            
            form.save()
            # messages.add_message(request, messages.SUCCESS, "Stock updated for %s" % store)
            form = StockForm()                
    else:
        form = StockForm()
        
    return render(request, 'agent_form.html', locals())

def pdt_page(request, pdt_id=None):
    if pdt_id == '0':
        products = Product.objects.all()        
    else:
        products = Product.objects.filter(id=int(pdt_id))        
    print(pdt_id)
    print(type(pdt_id))
    context = {
        'products':products
    }
    
    return render(request, 'products.html', context)

def store_admin(request):
    if request.POST:
        form = StoreForm(request.POST)
        if form.is_valid():            
            form.save()
            form = StoreForm()                
    else:
        form = StoreForm()
        
    return render(request, 'store_admin.html', locals())

def location_admin(request):
    if request.POST:
        form = LocationForm(request.POST)
        if form.is_valid():            
            form.save()
            form = LocationForm()                
    else:
        form = LocationForm()
        
    return render(request, 'location_admin.html', locals())

def agent_admin(request):
    if request.POST:
        form = AgentForm(request.POST)
        if form.is_valid():            
            form.save()
            form = AgentForm()                
    else:
        form = AgentForm()
        
    return render(request, 'agent_admin.html', locals())

def region_admin(request):
    if request.POST:
        form = RegionForm(request.POST)
        if form.is_valid():            
            form.save()
            form = RegionForm()                
    else:
        form = RegionForm()
        
    return render(request, 'region_admin.html', locals())