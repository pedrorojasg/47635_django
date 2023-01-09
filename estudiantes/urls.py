from django.urls import path

from estudiantes.views import listar_estudiantes, listar_profesores


urlpatterns = [
    path('alumnos/', listar_estudiantes, name="listar_alumnos"),
    path('profesores/', listar_profesores, name="listar_profesores"),
]
