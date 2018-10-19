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
	# Resultado posterior: Retorna True, la funcion fue definida para retornar el valor


	# Prueba 2. Caso frontera. Se llama la funcion registrarUsuario con un
	# correo electronico invalido, y dos claves validas e iguales.
	# El valor esperado es que la funcion retorne False y no almacene nada.

	def test_registrar_usuario_correo_invalido(self):
		self.assertFalse(self.seguridad.registrarUsuario("andresitorresm", "mmM123MJ", "mmM123MJ"))

	# Resultado de primera ejecucion: Falla porque retorna True y no False
	# Resultado de siguiente ejecucion: Retorna False, ahora se verifican los correos

	# Prueba 2.5. Casos frontera. Se llama a la funcion es_correo_valido
	# con dos correo electronico validos, uno invalido y uno vacio, para verificar
	# que la funcion auxiliar programada es correcta.
	# Los valores esperados son True, True, False y False

	def test_es_correo_valido(self):
		self.assertTrue(self.seguridad.es_correo_valido("andresitorresm@gmail.com"))
		self.assertTrue(self.seguridad.es_correo_valido("14-11082@usb.ve"))
		self.assertFalse(self.seguridad.es_correo_valido("14-11082"))
		self.assertFalse(self.seguridad.es_correo_valido(""))

	# Resultado de la primera ejecucion: La prueba pasa, se verifica que la funcion auxiliar es correcta

	

if __name__ == '__main__':
	unittest.main()