from django.db import models

from django.contrib.auth.models import User

class TaskCategory(models.Model):
	category = models.CharField(max_length=128)
	def __str__(self):
		return self.category

class TaskEntry(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	datetime = models.DateField(auto_now=True)
	description = models.CharField(max_length=128)
	completed = models.BooleanField(default=False)
	category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
