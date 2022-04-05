from django.db import models
from django.contrib.auth.models import User

class BudgetCategory(models.Model):
	category = models.CharField(max_length=128)
	def __str__(self):
		return self.category

class BudgetEntry(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	datetime = models.DateField(auto_now=True)
	description = models.CharField(max_length=128)
	projected = models.IntegerField(max_length=100)
	actual = models.IntegerField(max_length=100)
	category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)