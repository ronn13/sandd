#for deployment to openshift
from django.shortcuts import render
from django.contrib import messages
from forms import *
from models import *

def index(request):
    return render(request, 'index.html')

def store_totals(request, region=None):
    stores = []
    if region is None:
        return render(request, 'store_totals.html')
    else:
        locations = Location.objects.filter(region=region)
        for location in locations:
            stores.append(location_stores(location))
        return render(request, 'store_totals.html', {'stores':stores})        

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
