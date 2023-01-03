from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from estudiantes.models import Estudiante


def saludar(request):
    return HttpResponse(f'Hola comision 47635. Hora: {datetime.now()}')


def listar_estudiantes(request):
    contexto = {
        'estudiantes': Estudiante.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_estudiantes.html',
        context=contexto
    )


def listar_profesores(request):
    return render(request=request, template_name='estudiantes/lista_profesores.html')
