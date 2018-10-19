import re

'''
La clase Seguridad esta construida para permitir el registro
y la autenticacion de los usuarios siguiendo algunas reglas de seguridad.
'''
class Seguridad:

	def __init__(self):
		# NOTA: Se asume que el rango de claves es inclusivo,
		# es decir, que es valido tener 8 caracteres y que
		# es valido tener 16 caracteres

		self.longitud_minima = 8
		self.longitud_maxima = 16

	def registrarUsuario(self, email, clave1, clave2):
		return self.es_correo_valido(email) and self.es_clave_valida(clave1, clave2)

	def es_correo_valido(self, email):
		# El regex a continuacion interpreta el formato de correos
		# electronicos del estandar RFC 822, que tiene letras, numeros y
		# algunos simbolos especiales, seguidos de un arroba, y luego el
		# formato de un dominio de internet.
		if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
			return True
		return False

	def es_clave_valida(self, clave1, clave2):
		if not self.claves_coinciden(clave1, clave2):
			return False

		if not (self.clave_tiene_longitud_correcta(clave1) and self.clave_tiene_longitud_correcta(clave2)):
			return False

		return True 

	def claves_coinciden(self, clave1, clave2):
		return clave1 == clave2

	def clave_tiene_longitud_correcta(self, clave):
		tamano_clave = len(clave)
		return (self.longitud_minima <= tamano_clave) and (tamano_clave <= self.longitud_maxima)