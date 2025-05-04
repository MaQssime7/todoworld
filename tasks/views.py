from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import render, redirect, get_object_or_404

def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # redirige pour éviter le resoumission

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

# Suppression d'une tâche
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)

    # Vérifie si l'utilisateur est autorisé à supprimer la tâche
    if task:
        task.delete()

    return redirect('task_list')  # Redirige vers la liste des tâches après suppression