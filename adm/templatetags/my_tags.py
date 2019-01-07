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
	
@register.simple_tag
def get_products(keyword=None):
    return Product.objects.all()
	