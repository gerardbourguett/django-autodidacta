from django.urls import path

from myapp import views

urlpatterns = [
    path("", views.hola_mundo),
    path("about/", views.about),
]
