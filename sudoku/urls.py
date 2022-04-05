"""sudoku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views as app1_views
from journal import views as journal_views
from tasks import views as task_views
from budget import views as budget_views
urlpatterns = [
    path('', app1_views.home),
    path('admin/', admin.site.urls),
    path('rules/', app1_views.rules),
    path('about/', app1_views.about),
    path('join/', app1_views.join),
    path('login/', app1_views.user_login),
    path('logout/', app1_views.user_logout),
    path('journal/', journal_views.journal),
 	path('journal/add/', journal_views.add),
    path('journal/edit/<int:id>/', journal_views.edit),
    path('tasks/', task_views.task),
 	path('tasks/add/', task_views.add),
    path('tasks/edit/<int:id>/', task_views.edit),
    path('tasks/toggle/<int:id>/', task_views.toggle),
    path('budget/', budget_views.task),
 	path('budget/add/', budget_views.add),
    path('budget/edit/<int:id>/', budget_views.edit),
]
