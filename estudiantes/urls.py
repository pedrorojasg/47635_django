from django.urls import path

from estudiantes.views import (
    listar_profesores, listar_cursos,
    crear_curso, buscar_cursos, ver_curso, editar_curso, eliminar_curso,
    EstudianteListView
)


urlpatterns = [
    path('profesores/', listar_profesores, name="listar_profesores"),
    path('crear-curso/', crear_curso, name="crear_curso"),
    # URLS de cursos (basadas den views funcionales)
    path('cursos/', listar_cursos, name="listar_cursos"),
    path('buscar-cursos/', buscar_cursos, name="buscar_cursos"),
    path('cursos/<int:id>/', ver_curso, name="ver_curso"),
    path('editar-curso/<int:id>/', editar_curso, name="editar_curso"),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),
    # URLS de alumnos (basadas den Class Based Views, vistas basadas en clases)
    path('alumnos/', EstudianteListView.as_view(), name="listar_alumnos"),
]
