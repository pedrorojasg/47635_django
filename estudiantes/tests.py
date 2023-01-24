from django.test import TestCase

from estudiantes.models import Curso


class CursoTests(TestCase):
    """En esta clase van todas las pruebas del modelo Curso."""

    def test_creacion_de_curso(self):
        """
        Prueba crear cursos con nombres cortos y largos
        """
        curso_nombre_valido = Curso.objects.create(
            nombre="nombre corto", comision=101
        )
        # Compruebo que el curso fue creado
        self.assertEqual(Curso.objects.all().count(), 1)
        self.assertIsNotNone(curso_nombre_valido.id)
