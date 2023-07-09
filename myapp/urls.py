from django.urls import path

from myapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path(
        "hello/<str:username>", views.hola_mundo, name="hello"
    ),  # <str:username> es el nombre del usuario
    path("projects/", views.projects, name="projects"),
    path("projects/<int:id>", views.project_detail, name="project_detail"),
    path("tasks/", views.tasks, name="tasks"),
    path("create_task/", views.create_task, name="create_task"),
    path("create_project/", views.create_project, name="create_project"),
]
