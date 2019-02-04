from django import template
from adm.models import *

register = template.Library()

@register.simple_tag
def year_total(keyword):
	return list(Stock.objects.year_count(keyword).values())[0]

@register.simple_tag
def month_total(keyword):
	return list(Stock.objects.month_count(keyword).values())[0]

@register.simple_tag
def day_total(keyword):
	return list(Stock.objects.day_count(keyword).values())[0]

@register.simple_tag
def pdt_year_total(keyword):
	return list(Stock.objects.pdt_year_count(keyword).values())[0]

@register.simple_tag
def pdt_month_total(keyword):
	return list(Stock.objects.pdt_month_count(keyword).values())[0]

@register.simple_tag
def pdt_day_total(keyword):
	return list(Stock.objects.pdt_day_count(keyword).values())[0]

@register.simple_tag
def get_stock_type_display(keyword):
	return keyword.get_stock_type_display()
	
# get all products for use in the base.html nav menu
@register.simple_tag
def get_products(keyword=None):
    return Product.objects.all()

# get all regions for use in the base.html nav menu
@register.simple_tag
def get_all_regions(keyword=None):
    return Location.objects.all()

#a tag to retrieve the region from the store location
@register.simple_tag
def get_store_region(keyword=None):
	loc_object = Location.objects.get(name=keyword)
	return loc_object.region
	