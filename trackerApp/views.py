from django.shortcuts import render
from .models import Task

# Create your views here.
def task_list(request):
    task = Task.objects.all()
    return render(request, 'trackerApp/task_list.html', {'task': task})