from django import forms
from models import *

class ProductsForm(forms.ModelForm):
    STORES = (
        ('1', 'Father and Sons Depo'),
        ('2', 'Mother and Daughters Depo'))
    
    store = forms.ChoiceField(choices=STORES)
    shampoo = forms.IntegerField(initial=0)
    hairgel = forms.IntegerField(initial=0)
    relaxer = forms.IntegerField(initial=0)
    
    class Meta:
        model = Products 
        fields = ('store','shampoo','hairgel','relaxer')