from django.test import TestCase

from .models import Bar,Tapa

# Create your tests here.

class TestBarTestCase):

	def test_crear_bar(self):
		b = Bar(nombre="bar", direccion="direccion",numero_visita=0)
		b.save()
		self.assertEqual(b.nombre, "bar")
		print("Test: creación y salvado de bar correcto")

