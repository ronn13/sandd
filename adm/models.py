from django.db import models

class Store(models.Model):
    store_name = models.CharField(max_length=250)
    agent = models.ForeignKey('Agent')
    
    def __str__(self):
		return self.store_name

class Agent(models.Model):
	agent_names = models.CharField(max_length=50)
	region=models.CharField(max_length=50)

	def __str__(self):
		return self.agent_names

class Products(models.Model):
    stock_type = models.CharField(max_length=20, default="opening")
    shampoo = models.IntegerField()
    hairgel = models.IntegerField()
    relaxer = models.IntegerField()
    store = models.ForeignKey('Store')
    
    def __str__(self):
        return self.store
