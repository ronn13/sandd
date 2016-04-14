#for deployment to openshift
import datetime
from django.shortcuts import render
from django.contrib import messages
from forms import *
from models import *

def store_totals(request, region=None):
    stores = []
    day_stock = {}
    month_stock = {}
    year_stock = {}
    if region is None:
        region='Central'    
    locations = Location.objects.filter(region__name=region)
    for ltn in locations:
        for shop in Store.objects.filter(store_location__name=ltn):
            stores.append(shop)
            index = shop.store_name
            day_stock[index] = 0
            month_stock[index] = 0
            year_stock[index] = 0
            for stock in Stock.objects.filter(store__store_name=shop.store_name):
                if stock.stock_time.date().year == datetime.datetime.now().date().year: 
                    year_stock[index] = year_stock[index] + stock.stock_count                    
                if stock.stock_time.date().month == datetime.datetime.now().date().month: 
                    month_stock[index] = month_stock[index] + stock.stock_count                    
                if stock.stock_time.date().day == datetime.datetime.now().date().day: 
                    day_stock[index] = day_stock[index] + stock.stock_count
                    
    context = {
        'stores':stores,
        'region':region,
        'day_stock':day_stock,
        'month_stock':month_stock,
        'year_stock':year_stock 
    }
    return render(request, 'store_totals.html', context)        

def agents(request, region=None, agent=None):
    if region is None:
        return render(request, 'agents.html')
    else:
        if agent is None:
            region_agents = Agent.objects.get(region=region)
            return render(request, 'agents.html', {'region_agents':region_agents})
        else:
            region_agents = "nothing worth it"
            return render(request, 'agents.html', {'region_agents':region_agents})

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
