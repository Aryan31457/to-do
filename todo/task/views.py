from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import TaskForm
from .models import Task

# Create Task View
def create_Task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task:task_list')
        else:
            messages.error(request, 'There was an error with the form.')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

# Task List View (Updated)
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

# Edit Task View (New)
def edit_Task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task:task_list')
        else:
            messages.error(request, 'There was an error with the form.')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'edit_task.html', {'form': form, 'task': task})

# Delete Task View (New)
def delete_Task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task:task_list')
    
    return render(request, 'delete_task.html', {'task': task})
