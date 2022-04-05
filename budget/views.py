from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from budget.models import BudgetEntry, BudgetCategory
from budget.forms import BudgetEntryForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='/login/')
def task(request):
	if(BudgetCategory.objects.count() == 0):
		BudgetCategory(category = "Home").save()
		BudgetCategory(category = "School").save()
		BudgetCategory(category = "Work").save()
		BudgetCategory(category = "Self Improvement").save()
		BudgetCategory(category = "Other").save()

	if (request.method == "GET" and "delete" in request.GET):
		id = request.GET["delete"]
		BudgetEntry.objects.filter(id=id).delete()
		return redirect("/budget/")
	else:
		table_data = BudgetEntry.objects.filter(user=request.user)
		context = {
            "table_data": table_data
		}
		return render(request, 'budget/budget.html', context)

@login_required(login_url='/login/')
def add(request):
	if (request.method == "POST"):
		if ("add" in request.POST):
			form = BudgetEntryForm(request.POST)
			if (form.is_valid()):
				#description = form.cleaned_data["description"]
				#entry = form.cleaned_data["entry"]
				#category = form.cleaned_data["category"]
				#user = User.objects.get(id=request.user.id)
				#TaskEntry(user=user, category=category, description=description, entry=entry).save()
				BudgetEntry = form.save(commit=False)
				BudgetEntry.user = request.user
				BudgetEntry.save()
				return redirect("/budget/")
			else:
				context = {
                    "form_data": add_form
				}
				return render(request, 'budget/add.html', context)
		else:
			return redirect("/budget/")
	else:
		context = {
            "form_data": BudgetEntryForm()
		}
		return render(request, 'budget/add.html', context)

@login_required(login_url='/login/')
def edit(request, id):
	if (request.method == "GET"):
		budgetEntry = BudgetEntry.objects.get(id=id)
		form = BudgetEntryForm(instance= budgetEntry)
		context = {"form_data": form}
        
		return render(request, 'budget/edit.html', context)
	elif (request.method == "POST"):
		# Process form submission
		if ("edit" in request.POST):
			form = BudgetEntryForm(request.POST)
			if (form.is_valid()):
				budgetEntry = form.save(commit=False)
				budgetEntry.user = request.user
				budgetEntry.id = id
				budgetEntry.save()
				return redirect("/budget/")
			else:
				context = {
                    "form_data": form
				}
				return render(request, 'budget/add.html', context)
		else:
			#Cancel
			return redirect("/budget/")
