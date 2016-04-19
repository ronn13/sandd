import datetime
from django.db import models
from django.db.models import F, Sum

class Region(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
    def __unicode__(self):
        return '%s' % (self.name)

class Location(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey('Region')
    
    # def __str__(self):
    #     return self.name
        
    def __unicode__(self):
        return unicode(self.name)

class Agent(models.Model):
    username = models.CharField(max_length=50, unique=True)
    fist_name = models.CharField(max_length=50, default="First Name")
    last_name = models.CharField(max_length=50, default="Last Name")

    def __str__(self):
        return self.username    

class Store(models.Model):
    store_name = models.CharField(max_length=250)
    store_location = models.ForeignKey('Location')
    agent = models.ForeignKey('Agent')
       
    def __unicode__(self):
        return unicode(self.store_name)

class Product(models.Model):
    name = models.CharField(max_length=20, default="product name")
    unit_price = models.IntegerField()
    
    def __str__(self):
        return self.name
        
    def __unicode__(self):
        return '%s' % (self.name)

class StockManager(models.Manager):
    def year_count(self, keyword):
        return Stock.objects.filter(store__store_name=keyword).filter(stock_time__year=datetime.datetime.today().date().year).aggregate(Sum('stock_count'))
    #for month and day, datetime returns single digits without the leading zero. add if to add it if count is less than 2
    def month_count(self, keyword):
        return Stock.objects.filter(store__store_name=keyword).filter(stock_time__month=datetime.datetime.today().date().month).aggregate(Sum('stock_count'))
        
    def day_count(self, keyword):
        return Stock.objects.filter(store__store_name=keyword).filter(stock_time__day=datetime.datetime.today().date().day).aggregate(Sum('stock_count'))

class Stock(models.Model):
    CHOICES = (('1', 'Opening Stock'),
        ('2', 'Closing stock'),
        ('3', 'New stock'),)
    product = models.ForeignKey('Product')
    stock_count = models.IntegerField()
    store = models.ForeignKey('Store')
    stock_type = models.CharField(max_length=20, choices=CHOICES)
    stock_time = models.DateTimeField(auto_now_add=True)
    objects = StockManager()
    
    