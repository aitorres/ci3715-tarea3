# encoding=utf-8
from django.test import TestCase

# Se importa el modulo de PyUnit para realizar las 
# pruebas unitarias
import unittest 
from seguridad import Seguridad

################# Test Driven Development ################

class TestSeguridad(unittest.TestCase):

	def setUp(self):
		self.seguridad = Seguridad()

	def tearDown(self):
		self.seguridad = None

	# Prueba 1. Caso interior. Se llama la funcion registrarUsuario()
	# con un correo electronico valido y dos claves iguales.
	# Caso interior. El valor esperado es que la funcion retorne True
	# y almacene en el diccionario de Seguridad el usuario y la contraseña.

	def test_registrar_usuario_1(self):
		self.assertTrue(self.seguridad.registrarUsuario("andresitorresm@gmail.com","mmM123MJ","mmM123MJ"))
	
	# Resultado de primera ejecucion: Falla porque la funcion no esta definida.

if __name__ == '__main__':
	unittest.main()