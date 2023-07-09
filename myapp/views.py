from django.shortcuts import redirect, render  # render, get_object_or_404,
from django.http import HttpResponse, JsonResponse
from .models import Project, Task  # Create your models here.
from django.shortcuts import get_object_or_404, render  # get_object_or_40  # noqa: F811
from .forms import CreateNewTask, CreateNewProject  # Create your forms here.

# Create your views here.


def index(request):
    title = "Home"
    return render(request, "index.html", {"title": title})


def about(request):
    username = "gerard"
    return render(request, "about.html", {"username": username})


def hola_mundo(request, username):
    return HttpResponse("<h1>Hola %s</h1>" % username)


def projects(request):
    # projects = list(Project.objects.values())  # Obtener todos los proyectos)
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {"projects": projects})


def tasks(request):
    # task = get_object_or_404(Task, pk=id)
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {"form": CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=2,
        )
        redirect("tasks")


def create_project(request):
    if request.method == "GET":
        return render(
            request, "projects/create_project.html", {"form": CreateNewProject()}
        )
    else:
        Project.objects.create(
            name=request.POST["name"],
            description=request.POST["description"],
        )
        redirect("projects")

def project_detail(request, id):
    project = get_object_or_404(Project, pk=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, "projects/project_detail.html", {"project": project, "tasks": tasks})