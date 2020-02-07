from django import template
from adm.models import *

register = template.Library()

# yearly totals for store with store passed as keyword
@register.simple_tag
def year_total(keyword):
	return list(Stock.objects.year_count(keyword).values())[0]

# monthly totals for store with store passed as keyword
@register.simple_tag
def month_total(keyword):
	return list(Stock.objects.month_count(keyword).values())[0]

# daily totals for store with store passed as keyword
@register.simple_tag
def day_total(keyword):
	return list(Stock.objects.day_count(keyword).values())[0]

# yearly totals for product with product passed as keyword
@register.simple_tag
def pdt_year_total(keyword):
	return list(Stock.objects.pdt_year_count(keyword).values())[0]

# monthly totals for product with product passed as keyword
@register.simple_tag
def pdt_month_total(keyword):
	return list(Stock.objects.pdt_month_count(keyword).values())[0]

# daily totals for product with product passed as keyword
@register.simple_tag
def pdt_day_total(keyword):
	return list(Stock.objects.pdt_day_count(keyword).values())[0]

# total stock for the whole year
@register.simple_tag
def total_year_total():
	return list(Stock.objects.total_year_count().values())[0]

# total stock for the whole month
@register.simple_tag
def total_month_total():
	return list(Stock.objects.total_month_count().values())[0]

# total stock for the whole day
@register.simple_tag
def total_day_total():
	return list(Stock.objects.total_day_count().values())[0]

# monthly total stock per region with region passed as keyword
@register.simple_tag
def region_month_total(keyword)
    return list(Stock.objects.region_month_count(keyword).values())[0]

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
	