import datetime
from django.db import models
from django.db.models import F, Sum

class Region(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey('Region', on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name

class Agent(models.Model):
    username = models.CharField(max_length=50, unique=True)
    fist_name = models.CharField(max_length=50, default="First Name")
    last_name = models.CharField(max_length=50, default="Last Name")

    def __str__(self):
        return self.username    

class Store(models.Model):
    store_name = models.CharField(max_length=250)
    store_location = models.ForeignKey('Location', on_delete= models.CASCADE)
    agent = models.ForeignKey('Agent', on_delete= models.CASCADE)
       
    def __str__(self):
        return self.store_name

class Product(models.Model):
    name = models.CharField(max_length=20, default="product name")
    unit_price = models.IntegerField()
    
    def __str__(self):
        return self.name

class StockManager(models.Manager):
    # totals per month/day/year per store
    def year_count(self, keyword):
        return Stock.objects.filter(store__store_name=keyword).filter(stock_time__year=datetime.datetime.today().date().year).aggregate(Sum('stock_count'))
    #for month and day, datetime returns single digits without the leading zero. add if to add it if count is less than 2
    def month_count(self, keyword):
        return Stock.objects.filter(store__store_name=keyword).filter(stock_time__month=datetime.datetime.today().date().month).aggregate(Sum('stock_count'))
        
    def day_count(self, keyword):
        return Stock.objects.filter(store__store_name=keyword).filter(stock_time__day=datetime.datetime.today().date().day).aggregate(Sum('stock_count'))

    # totals per month/day/year per product
    def pdt_year_count(self, keyword):
        return Stock.objects.filter(product__name=keyword).filter(stock_time__year=datetime.datetime.today().date().year).aggregate(Sum('stock_count'))
    #for month and day, datetime returns single digits without the leading zero. add if to add it if count is less than 2
    def pdt_month_count(self, keyword):
        return Stock.objects.filter(product__name=keyword).filter(stock_time__month=datetime.datetime.today().date().month).aggregate(Sum('stock_count'))
        
    def pdt_day_count(self, keyword):
        return Stock.objects.filter(product__name=keyword).filter(stock_time__day=datetime.datetime.today().date().day).aggregate(Sum('stock_count'))

    # totals per year/month/day for all stores for all products 
    def total_year_count(self, keyword):
        return Stock.objects.all().filter(stock_time__year=datetime.datetime.today().date().year).aggregate(Sum('stock_count'))
    #for month and day, datetime returns single digits without the leading zero. add if to add it if count is less than 2
    def total_month_count(self, keyword):
        return Stock.objects.all().filter(stock_time__month=datetime.datetime.today().date().month).aggregate(Sum('stock_count'))
        
    def total_day_count(self, keyword):
        return Stock.objects.all().filter(stock_time__day=datetime.datetime.today().date().day).aggregate(Sum('stock_count'))

class Stock(models.Model):
    CHOICES = (('opening', 'Opening Stock'),
        ('closing', 'Closing stock'),
        ('new', 'New stock'),)

    product = models.ForeignKey('Product', related_name='products', on_delete= models.CASCADE)
    stock_count = models.IntegerField()
    store = models.ForeignKey('Store', related_name='stores', on_delete= models.CASCADE)
    stock_type = models.CharField(max_length=20, choices=CHOICES)
    stock_time = models.DateTimeField(auto_now_add=True)
    
    objects = StockManager()
    
    #one store can only have one stock type ie opening stock per week.
    #time period for this would need to be discussed with client
    class Meta:
        unique_together = ['store', 'stock_type', 'stock_time']


    def __str__(self):
        return self.store + self.stock_type + self.stock_time
    