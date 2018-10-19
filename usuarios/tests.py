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


	# Prueba 3. Caso frontera. Se llama la funcion registrarUsuario con un correo electronico
	# valido pero con dos claves que no coinciden. Se espera que la funcion
	# retorne False ya que las claves no son la misma.

	def test_registrar_usuario_claves_distintas(self):
		self.assertFalse(self.seguridad.registrarUsuario("mariagrimaldi@gmail.com", "mmM123MK", "mmM132MJ"))

	# Resultado de primera ejecucion: Falla porque la funcion solo verifica si el correo
	# es valido o no
	# Resultado de la siguiente ejecucion: Pasa, porque ahora se verifica
	# que ambas claves sean la misma

	# Prueba 3.5. Casos frontera. Se llama a la funcion claves_coinciden con
	# dos pares de claves que coinciden, un par que no coincide, y dos pares de claves que
	# alternan una estar vacia y la otra no, para verificar que la funcion
	# auxiliar programada es correcta.
	# Los valores esperados son True, True, False, False, False.

	def test_claves_coinciden(self):
		self.assertTrue(self.seguridad.claves_coinciden("clave1", "clave1"))
		self.assertTrue(self.seguridad.claves_coinciden("4m1g0LDC", "4m1g0LDC"))
		self.assertFalse(self.seguridad.claves_coinciden("clave1", "clave2"))
		self.assertFalse(self.seguridad.claves_coinciden("clave1", ""))
		self.assertFalse(self.seguridad.claves_coinciden("", "clave2"))

	# Resultado de la primera ejecucion: Las pruebas pasan, y se verifica que la
	# funcion auxiliar claves_coinciden cumplen con su cometido


	# Prueba 4. Caso interior. Verificacion de longitud. Se llama la funcion
	# con un correo electronico valido y dos claves que coinciden pero
	# que estan por debajo o por encima del tamano permitido. Los valores esperados
	# en las dos pruebas a realizar son False y False.

	def test_registrar_usuario_longitud_claves(self):
		self.assertFalse(self.seguridad.registrarUsuario("andresitorresm@gmail.com", "m1", "m1"))
		self.assertFalse(self.seguridad.registrarUsuario("andresitorresm@gmail.com", "mmmmmJJJJJ1111133333", "mmmmmJJJJJ1111133333"))

	# Resultado de primera ejecucion: Falla porque las claves coinciden y eso es todo lo
	# que se valida hasta este punto.
	# Resultado de siguiente ejecucion: Pasa, ya se valida la longitud de las
	# claves.

	# Prueba 4.5. Casos frontera. Se verifica el correcto funcionamiento de la
	# funcion auxiliar tiene_longitud_correcta para conocer si la funcion labora
	# de la manera correcta, con dos pares de contraseñas de longitud correcta,
	# y dos pares de contraseñas de longitud incorrecta.
	# Los resultados esperados son True, True y False, False

	def test_longitud_correcta(self):
		self.assertTrue(self.seguridad.clave_tiene_longitud_correcta("holaAmigo"))
		self.assertTrue(self.seguridad.clave_tiene_longitud_correcta("hola12345687"))
		self.assertFalse(self.seguridad.clave_tiene_longitud_correcta("clave"))
		self.assertFalse(self.seguridad.clave_tiene_longitud_correcta("hola_estaes_una_clave_muy_larga"))

	# Resultado de la primera ejecucion: las pruebas pasan porque la funcion se desempeña
	# de la manera correcta


	# Prueba 5. Caso interior. Verificacion de caracteres especiales. Se llama la funcion
	# registrarUsuario con un correo electronico valido y claves que coinciden de igual longitud
	# pero que incluyen simbolos especiales.
	# El valor esperado es False, ya que solo se permiten numeros y letras en la clave.

	def test_claves_caracteres_especiales(self):
		self.assertFalse(self.seguridad.registrarUsuario("andresitorresm@gmail.com", "hola1234_", "hola1234_"))
		self.assertFalse(self.seguridad.registrarUsuario("andresitorresm@gmail.com", "@m_g1.-_{", "@m_g1.-_{"))

	# Resultado de la primera ejecucion: la prueba falla porque devuelve True, no se verifica
	# que solo se permitan utilizar letras y numeros en las claves
	# Resultado de la siguiente ejecucion: la prueba pasa porque ya verifica
	# si la clave tiene simbolos permitidos

	# Prueba 5.5. Verificacion de simbolos permitidos. Se llama la funcion
	# clave_tiene_simbolos_permitidos con dos claves con simbolos validos y dos claves
	# con simbolos invalidos para conocer si la funcion creada se comporta
	# como deberia. Los resultados esperados son True, True, False, False.

	def test_simbolos_especiales(self):
		self.assertTrue(self.seguridad.clave_tiene_simbolos_permitidos("amigo"))
		self.assertTrue(self.seguridad.clave_tiene_simbolos_permitidos("jfgnr1574"))
		self.assertFalse(self.seguridad.clave_tiene_simbolos_permitidos("amigo-"))
		self.assertFalse(self.seguridad.clave_tiene_simbolos_permitidos("4_$/#$%&1"))

	# Resultado de la primera ejecucion: las pruebas pasan, por lo que la funcion
	# verifica correctamente que solo se tengan simbolos del conjunto permitido

	# Prueba 6. Se verifica que la clave debe contener ciertos patrones en las
	# letras, a saber: al menos tres letras, de esas al menos una minuscula y una mayuscula.
	# Se ejecuta la funcion con una clave que cumple con estos parametros y
	# tres pares que no cumplen. El valor esperado es True para el primer caso y False para los
	# otros tres. Esta prueba seria de interior y frontera.

	def test_requerimientos_en_letras(self):
		self.assertTrue(self.seguridad.registrarUsuario("andresitorresm@gmail.com", "aAama1234", "aAama1234"))
		self.assertFalse(self.seguridad.registrarUsuario("14-11082@usb.ve", "aA123456", "aA123456"))
		self.assertFalse(self.seguridad.registrarUsuario("mariagrimaldi@outlook.com", "aa11bb22", "aa11bb22"))
		self.assertFalse(self.seguridad.registrarUsuario("amigo@correo.com", "12345678", "12345678"))

	# Resultado de la primera ejecucion: La prueba falla porque todo retorna True, no se validan las
	# condiciones de letras.
	# Resultado de la segunda ejecucion: La prueba pasa ya que se verifican las
	# cantidades de letras segun lo establecido.

	# Prueba 6.5. Verificacion de funcion de letras minimas. Se ejecutan pruebas
	# varias para la funcion clave_tiene_letras_minimas, con tres casos de claves que
	# tienen las letras validas y tres que no las tienen. Se espera como resultado
	# True, True, True, False, False, False. Estas pruebas son de frontera.

	def test_letras_minimas(self):
		self.assertTrue(self.seguridad.clave_tiene_letras_minimas("aaB"))
		self.assertTrue(self.seguridad.clave_tiene_letras_minimas("amiGote1234"))
		self.assertTrue(self.seguridad.clave_tiene_letras_minimas("BBr"))
		self.assertFalse(self.seguridad.clave_tiene_letras_minimas("aa"))
		self.assertFalse(self.seguridad.clave_tiene_letras_minimas("a1234124"))
		self.assertFalse(self.seguridad.clave_tiene_letras_minimas("Ax12581879"))

	# Resultado de la primera ejecucion: La prueba se ejecuta correctamente verificando que la
	# funcion de verificacion de letras minimas esta correcta.

	
	# Prueba 7. Se ejecuta la funcion registrarUsuario con una clave que no
	# tiene digitos, conociendo que las claves deben tener al menos un digito como
	# condicion minima de validez. Se llama con dos casos de prueba, uno que cumple con
	# tener al menos un digito y otro que no lo tiene pero que cumplen con el
	# resto de criterios. La prueba seria de interior y de frontera. Se espera que 
	# los valores sean True, False.

	def test_tiene_digitos_minimos(self):
		self.assertTrue(self.seguridad.registrarUsuario("14-11085@usb.ve", "1amiGuito", "1amiGuito"))
		self.assertFalse(self.seguridad.registrarUsuario("12354@correo.com", "amiGOami", "amiGOami"))

	# Resultado de la primera ejecucion: La prueba se ejecuta y falla, ya que acepta todas las claves
	# a pesar de que uan no tiene digitos.

if __name__ == '__main__':
	unittest.main()