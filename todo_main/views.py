from django.shortcuts import render
from todo.models import Task as task
def home(request):
    tasks = task.objects.filter(is_completed=False).order_by('-updated_at')
    compiled_tasks = task.objects.filter(is_completed=True).order_by('-updated_at')
    context = {'tasks':tasks,
               'compiled_tasks':compiled_tasks
               }

    return render(request, 'home.html', context)
