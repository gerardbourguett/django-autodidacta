from django.urls import path

from myapp import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path(
        "hello/<str:username>", views.hola_mundo
    ),  # <str:username> es el nombre del usuario
    path("projects/", views.projects),
    path("tasks/<str:title>", views.tasks),
]
