from django.forms import ModelForm
from .models import *

class ProductsForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'

class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = '__all__'