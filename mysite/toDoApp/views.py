from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def todo(request):
    template = loader.get_template('toDoApp/todo.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('toDoApp/home.html')
    return HttpResponse(template.render())
