from django.http import HttpResponse
from app1.models import Board
from app1.forms import SudokuForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app1.forms import SudokuForm, JoinForm, LoginForm
from django.contrib.auth.decorators import login_required
from budget.models import BudgetEntry
from tasks.models import TaskEntry
@login_required(login_url='/login/')
def home(request):
    budgets = BudgetEntry.objects.filter(user=request.user)
    mainBudgets = []
    projectedBudgets = []

    for budget in budgets:
        mainBudgets.append(budget.projected)
        projectedBudgets.append(budget.actual)

    tasks = TaskEntry.objects.filter(user=request.user)
    notCompleted =0
    total =0
    for task in tasks:
        total += 1
        if not task.completed:
            notCompleted += 1
    page_data = {
        "budget": budgets,
        "task": tasks,
        "totalTasks": total,
        "notCompleted": notCompleted,
        "mainBudgets": mainBudgets,
        "projectedBudgets": projectedBudgets
    }
    print(page_data)
    return render(request, 'app1/home.html', page_data)

def rules(request):
    return render(request, 'app1/rules.html')

def about(request):
    return render(request, 'app1/about.html')

def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            page_data = { "join_form": join_form }
            return render(request, 'app1/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'app1/join.html', page_data)

def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request,user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'app1/login.html', {"login_form": LoginForm})
    else:
        #Nothing has been provided for username or password.
        return render(request, 'app1/login.html', {"login_form": LoginForm})

@login_required(login_url='/login/')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")
