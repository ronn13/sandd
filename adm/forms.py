from django import forms
from models import *

class ProductsForm(forms.ModelForm):
    STOCK_TYPES = (
        ('opening', 'Opening Stock'),
        ('closing', 'Closing Stock'),
        ('new', 'New Stock')
    )
    
    shampoo = forms.IntegerField(initial=0)
    hairgel = forms.IntegerField(initial=0)
    relaxer = forms.IntegerField(initial=0)
    stock_type = forms.ChoiceField(choices=STOCK_TYPES, widget=forms.RadioSelect())
    
    class Meta:
        model = Products 
        fields = ('store','shampoo','hairgel','relaxer','stock_type')