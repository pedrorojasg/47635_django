from django.urls import path

from estudiantes.views import saludar, listar_estudiantes


urlpatterns = [
    path('lista/', listar_estudiantes),
    path('saludar/', saludar),
]
