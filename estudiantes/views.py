from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime


def saludar(request):
    return HttpResponse(f'Hola comision 47635. Hora: {datetime.now()}')
