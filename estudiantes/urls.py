from django.urls import path

from estudiantes.views import saludar


urlpatterns = [
    path('saludar/', saludar),
    path('saludar2/', saludar),
    path('saludar3/', saludar),
]
