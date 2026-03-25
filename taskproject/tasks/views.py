from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

class TaskForm(forms.ModelForm):
    class Meta:    
        model = Task
        fields = ['title', 'description', 'completed']

#REGIDSTRATION VIEW

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

#LOGIN VIEW
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

#LOGOUT
def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def task_create(request):     #post
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            #create task but dont upload to database
            task = form.save(commit=False)
            #assign task to the current user
            task.user = request.user
            #now save to the database
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()   
    return render(request, 'tasks/tasks_list.html', {'form': form}) 

def is_admin(user):
#Check if user is admin/superuser
    return user.is_superuser or user.is_staff

#HOME VIEW
@login_required
def task_list(request):
    # If user is admin, show ALL tasks
    if is_admin(request.user):
        tasks = Task.objects.all()
        is_admin_view = True
    else:
        # Regular user sees only their tasks
        tasks = Task.objects.filter(user=request.user)
        is_admin_view = False
   
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks, 'is_admin': is_admin_view})

@login_required
def task_update(request, id): #update
    # If user is admin, they can edit any task
    if is_admin(request.user):
        task = get_object_or_404(Task, id=id)
    else:
        # Regular user can only edit their own tasks
        task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/tasks_list.html', {'form': form})

@login_required    
def task_delete(request, id):
    # If user is admin, they can delete any task
    if is_admin(request.user):
        task = get_object_or_404(Task, id=id)
    else:
        # Regular user can only delete their own tasks
        task = get_object_or_404(Task, id=id, user=request.user)
        
    task.delete()
    return redirect('task_list')

# Create your views here.
