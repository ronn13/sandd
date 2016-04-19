from django import template
from adm.models import *

register = template.Library()

@register.simple_tag
def year_total(keyword):
	return Stock.objects.year_count(keyword).values()[0]

@register.simple_tag
def month_total(keyword):
	return Stock.objects.month_count(keyword).values()[0]

@register.simple_tag
def day_total(keyword):
	return Stock.objects.year_count(keyword).values()[0]

@register.simple_tag
def get_stock_type_display(keyword):
	return keyword.get_stock_type_display()