from django.shortcuts import render,redirect
from .models import Task
from .form import TaskForm

# Create your views here.

def home(request):
    completed = Task.objects.filter(is_completed=True)
    card = Task.objects.filter(is_completed=False)
    return render(request, 'index.html', {'card': card, 'completed': completed, 'form' : TaskForm})
def completed_tasks(request,id):
    completed_tasks = Task.objects.get(id=id)
    completed_tasks.is_completed = not completed_tasks.is_completed
    completed_tasks.save()
    return redirect('home')
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')
def edit_task(request,id):
    task = Task.objects.get(id=id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
        
    return redirect('home')


def add_task(request):  
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return redirect('home')



# views.py
from rest_framework import viewsets
from .serializers import TaskSerializer,TaskSerializerCreate

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskSerializerCreate
        return TaskSerializer
