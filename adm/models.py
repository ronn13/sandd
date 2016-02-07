from django.db import models

class Agent(models.Model):
	agent_names = models.CharField(max_length=50)
	region=models.CharField(max_length=50)

	def __str__(self):
		return self.agent_names

class Products(modes.Model):
	shampoo = models.IntegerField(max_length=50)
	hairgel = models.IntegerField(max_length=50)
	relaxer = models.IntegerField(max_length=50)
	agent = models.ForeignKey('Agent')