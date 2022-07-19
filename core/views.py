from django.shortcuts import redirect, render
from .models import Tasks
from .forms import TasksForm, UpdateForm, CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    
    return render(request, 'login.html')

    
def signup(request):
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' +user)
            return redirect('login')
        else:
            messages.info(request, "please enther correct information and enter the unique username and strong password")


    form = CreateUserForm()
    context={'form': form}
    return render(request, 'signup.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def home(request):
    tasks = Tasks.objects.filter(user = request.user)
    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def updatetask(request, pk):
    task = Tasks.objects.get(id=pk)
    form = UpdateForm(instance=task)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'update.html', context)


@login_required(login_url='login')
def deletetask(request, pk):
    item = Tasks.objects.get(id = pk)
    item.delete()
    return redirect('home')

    
@login_required(login_url='login')
def completetask(request, pk):
    item = Tasks.objects.get(id = pk)
    item.complete = True
    item.save()
    return redirect('home')