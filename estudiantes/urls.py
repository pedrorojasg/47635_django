from django.urls import path

from estudiantes.views import saludar, listar_estudiantes, listar_profesores


urlpatterns = [
    path('saludar/', saludar),
    path('lista-alumnos/', listar_estudiantes, name="listar_alumnos"),
    path('lista-profesores/', listar_profesores, name="listar_profesores"),
]
