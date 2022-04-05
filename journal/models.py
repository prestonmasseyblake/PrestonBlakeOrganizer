from django.db import models
from django.contrib.auth.models import User

class JournalCategory(models.Model):
	category = models.CharField(max_length=128)
	def __str__(self):
		return self.category

class JournalEntry(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	datetime = models.DateField(auto_now=True)
	description = models.CharField(max_length=128)
	entry = models.CharField(max_length=65536)
	category = models.ForeignKey(JournalCategory, on_delete=models.CASCADE)
