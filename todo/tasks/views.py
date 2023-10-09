# from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    context = {'tasks':tasks}
    return render(request, 'tasks/list.html', context)
