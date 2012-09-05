from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.template import defaultfilters

@csrf_protect
def index(request):
    if request.method == 'POST': 
        task = Task(name=request.REQUEST['name'])
        task.save()
    tasks = Task.objects.all()
    return render(request, 'todo.html', {'tasks': tasks})
        
@csrf_protect
def update_task(request, id):
    if request.method == 'GET':
        task = Task.objects.get(id=id)
        task.finished = True
        task.save()
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        Task.objects.get(id=id).delete()
        return HttpResponseRedirect('/')
        