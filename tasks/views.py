from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from tasks.models import TaskEntry, TaskCategory
from tasks.forms import TaskEntryForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='/login/')
def task(request):
	if(TaskCategory.objects.count() == 0):
		TaskCategory(category = "Home").save()
		TaskCategory(category = "School").save()
		TaskCategory(category = "Work").save()
		TaskCategory(category = "Self Improvement").save()
		TaskCategory(category = "Other").save()

	if (request.method == "GET" and "delete" in request.GET):
		id = request.GET["delete"]
		TaskEntry.objects.filter(id=id).delete()
		return redirect("/tasks/")
	else:
		table_data = TaskEntry.objects.filter(user=request.user)
		context = {
            "table_data": table_data
		}
		return render(request, 'tasks/tasks.html', context)

@login_required(login_url='/login/')
def add(request):
	if (request.method == "POST"):
		if ("add" in request.POST):
			form = TaskEntryForm(request.POST)
			if (form.is_valid()):
				#description = form.cleaned_data["description"]
				#entry = form.cleaned_data["entry"]
				#category = form.cleaned_data["category"]
				#user = User.objects.get(id=request.user.id)
				#TaskEntry(user=user, category=category, description=description, entry=entry).save()
				TaskEntry = form.save(commit=False)
				TaskEntry.user = request.user
				TaskEntry.save()
				return redirect("/tasks/")
			else:
				context = {
                    "form_data": add_form
				}
				return render(request, 'tasks/add.html', context)
		else:
			# Cancel
			return redirect("/tasks/")
	else:
		context = {
            "form_data": TaskEntryForm()
		}
		return render(request, 'tasks/add.html', context)

@login_required(login_url='/login/')
def edit(request, id):
	if (request.method == "GET"):
		# Load Journal Entry Form with current model data.
		taskEntry = TaskEntry.objects.get(id=id)
		print(taskEntry.category)
		form = TaskEntryForm(instance=taskEntry)
		print(form)
		context = {"form_data": form}
        
		return render(request, 'tasks/edit.html', context)
	elif (request.method == "POST"):
		# Process form submission
		if ("edit" in request.POST):
			form = TaskEntryForm(request.POST)
			if (form.is_valid()):
                
				taskEntry = form.save(commit=False)
				taskEntry.user = request.user
				taskEntry.id = id
				taskEntry.save()
				return redirect("/tasks/")
			else:
				context = {
                    "form_data": form
				}
				return render(request, 'tasks/add.html', context)
		else:
			#Cancel
			return redirect("/tasks/")

@login_required(login_url='/login/')
def toggle(request, id):
	if (request.method == "POST"):
			taskEntrytoggle = TaskEntry.objects.get(id=id)
			if taskEntrytoggle.completed:
				taskEntrytoggle.completed = False
			else:
				taskEntrytoggle.completed = True
			taskEntrytoggle.save()
			return redirect("/tasks/")
			
