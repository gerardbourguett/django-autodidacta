from django.shortcuts import render  # render, get_object_or_404,
from django.http import HttpResponse, JsonResponse  # , HttpResponseRedirect
from .models import Project, Task  # Create your models here.
from django.shortcuts import get_object_or_404  # get_object_or_40

# Create your views here.


def hola_mundo(request, username):
    return HttpResponse("<h1>Hola %s</h1>" % username)


def about(request):
    return HttpResponse("<h1>About</h1>")


def index(request):
    return HttpResponse("<h1>Index</h1>")


def projects(request):
    projects = list(Project.objects.values())  # Obtener todos los proyectos)
    return JsonResponse(projects, safe=False)


def tasks(request, title):
    task = get_object_or_404(Task, pk=id)
    return HttpResponse("task: %s" % task.title)
