from django.contrib import admin
from budget.models import BudgetCategory, BudgetEntry

# Register your models here.
admin.site.register(BudgetCategory)
admin.site.register(BudgetEntry)