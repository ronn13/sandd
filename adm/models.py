from django.db import models

class Agent(models.Model):
	agent_names = models.CharField(max_length=50)
	region=models.CharField(max_length=50)

	def __str__(self):
		return self.agent_names

class StoreManager(models.Manager):
    def agent_stores(self, keyword):
        return self.filter(agent=keyword)

class Store(models.Model):
    store_name = models.CharField(max_length=250)
    agent = models.ForeignKey('Agent')
       
    def __str__(self):
		return self.store_name

class Product(models.Model):
    name = models.CharField(max_length=20, default="product name")
    unit_price = models.IntegerField()
    
    def __str__(self):
        return self.name

class StockManager(models.Manager):
    def store_stock(self, keyword):
        return self.filter(store_name=keyword).aggregate(Sum(count()))

class Stock(models.Model):
    CHOICES = (('1', 'Opening Stock'),
        ('2', 'Closing stock'),
        ('3', 'New stock'),)
    product = models.ForeignKey('Product')
    stock_count = models.IntegerField()
    store_name = models.ForeignKey('Store')
    stock_type = models.CharField(max_length=20, choices=CHOICES)
    stock_time = models.DateTimeField(auto_now_add=True)
    objects = StockManager()
    
    