from django.urls import path

from estudiantes.views import (
    listar_profesores, listar_cursos,
    crear_curso, buscar_cursos, ver_curso, editar_curso, eliminar_curso,
    EstudianteListView, EstudianteCreateView, EstudianteUpdateView,
    EstudianteDeleteView, EstudianteDetailView
)


urlpatterns = [
    path('profesores/', listar_profesores, name="listar_profesores"),
    # URLS de cursos (basadas den views funcionales)
    path('cursos/', listar_cursos, name="listar_cursos"),
    path('cursos/<int:id>/', ver_curso, name="ver_curso"),
    path('buscar-cursos/', buscar_cursos, name="buscar_cursos"),
    path('crear-curso/', crear_curso, name="crear_curso"),
    path('editar-curso/<int:id>/', editar_curso, name="editar_curso"),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),
    # URLS de estudiantes (basadas den Class Based Views, vistas basadas en clases)
    path('estudiantes/', EstudianteListView.as_view(), name="listar_estudiantes"),
    path('estudiantes/<int:pk>/', EstudianteDetailView.as_view(), name="ver_estudiante"),
    path('crear-estudiante/', EstudianteCreateView.as_view(), name="crear_estudiante"),
    path('editar-estudiante/<int:pk>/', EstudianteUpdateView.as_view(), name="editar_estudiante"),
    path('eliminar-estudiante/<int:pk>/', EstudianteDeleteView.as_view(), name="eliminar_estudiante"),
]
