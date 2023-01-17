from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from estudiantes.models import Estudiante, Profesor, Curso
from estudiantes.forms import CursoFormulario


def inicio(request):
    return render(
        request=request,
        template_name='estudiantes/inicio.html',
    )


# def listar_estudiantes(request):
#     ## Aqui iria la validacion del permiso lectura estudiantes
#     contexto = {
#         'estudiantes': Estudiante.objects.all()
#     }
#     return render(
#         request=request,
#         template_name='estudiantes/lista_estudiantes.html',
#         context=contexto,
#     )


def listar_profesores(request):
    contexto = {
        'profesores': Profesor.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_profesores.html',
        context=contexto,
    )


def listar_cursos(request):
    contexto = {
        'cursos': Curso.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_cursos.html',
        context=contexto,
    )


def ver_curso(request, id):
    curso = Curso.objects.get(id=id)
    contexto = {
        'curso': curso
    }
    return render(
        request=request,
        template_name='estudiantes/detalle_curso.html',
        context=contexto,
    )


def crear_curso_version_1(request):
    """No la estamos usando"""
    if request.method == "POST":
        data = request.POST
        curso = Curso(nombre=data['nombre'], comision=data['comision'])
        curso.save()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)
    else:  # GET
        return render(
            request=request,
            template_name='estudiantes/formulario_curso_a_mano.html',
        )


def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['nombre'], comision=data['comision'], descripcion=data['descripcion'])
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = CursoFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_curso.html',
        context={'formulario': formulario},
    )


def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso.nombre = data['nombre']
            curso.comision = data['comision']
            curso.descripcion = data['descripcion']
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': curso.nombre,
            'comision': curso.comision,
            'descripcion': curso.descripcion,
        }
        formulario = CursoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='estudiantes/formulario_curso.html',
        context={'formulario': formulario, 'curso': curso, 'es_update': True},
    )


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)


def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(comision__exact=data['busqueda'])
        )
        contexto = {
            'cursos': cursos
        }
        return render(
            request=request,
            template_name='estudiantes/lista_cursos.html',
            context=contexto,
        )


class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiantes/lista_estudiantes.html'


class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('listar_alumnos')


class EstudianteDetailView(DetailView):
    model = Estudiante
    success_url = reverse_lazy('listar_alumnos')


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('listar_alumnos')


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('listar_alumnos')
