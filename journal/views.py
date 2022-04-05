from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from journal.models import JournalEntry, JournalCategory
from journal.forms import JournalEntryForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='/login/')
def journal(request):
	if(JournalCategory.objects.count() == 0):
		JournalCategory(category = "Home").save()
		JournalCategory(category = "School").save()
		JournalCategory(category = "Work").save()
		JournalCategory(category = "Self Improvement").save()
		JournalCategory(category = "Other").save()

	if (request.method == "GET" and "delete" in request.GET):
		id = request.GET["delete"]
		JournalEntry.objects.filter(id=id).delete()
		return redirect("/journal/")
	else:
		table_data = JournalEntry.objects.filter(user=request.user)
		context = {
            "table_data": table_data
		}
		return render(request, 'journal/journal.html', context)

@login_required(login_url='/login/')
def add(request):
	if (request.method == "POST"):
		if ("add" in request.POST):
			form = JournalEntryForm(request.POST)
			if (form.is_valid()):
				#description = form.cleaned_data["description"]
				#entry = form.cleaned_data["entry"]
				#category = form.cleaned_data["category"]
				#user = User.objects.get(id=request.user.id)
				#JournalEntry(user=user, category=category, description=description, entry=entry).save()
				journalEntry = form.save(commit=False)
				journalEntry.user = request.user
				journalEntry.save()
				return redirect("/journal/")
			else:
				context = {
                    "form_data": add_form
				}
				return render(request, 'journal/add.html', context)
		else:
			# Cancel
			return redirect("/journal/")
	else:
		context = {
            "form_data": JournalEntryForm()
		}
		return render(request, 'journal/add.html', context)

@login_required(login_url='/login/')
def edit(request, id):
	if (request.method == "GET"):
		# Load Journal Entry Form with current model data.
		journalEntry = JournalEntry.objects.get(id=id)
		form = JournalEntryForm(instance=journalEntry)
		context = {"form_data": form}
		return render(request, 'journal/edit.html', context)
	elif (request.method == "POST"):
		# Process form submission
		if ("edit" in request.POST):
			form = JournalEntryForm(request.POST)
			if (form.is_valid()):
				journalEntry = form.save(commit=False)
				journalEntry.user = request.user
				journalEntry.id = id
				journalEntry.save()
				return redirect("/journal/")
			else:
				context = {
                    "form_data": form
				}
				return render(request, 'journal/add.html', context)
		else:
			#Cancel
			return redirect("/journal/")
