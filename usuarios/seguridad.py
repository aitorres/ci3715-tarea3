import re

'''
La clase Seguridad esta construida para permitir el registro
y la autenticacion de los usuarios siguiendo algunas reglas de seguridad.
'''
class Seguridad:

	def __init__(self):
		pass

	def registrarUsuario(self, email, clave1, clave2):
		return self.es_correo_valido(email)

	def es_correo_valido(self, email):
		# El regex a continuacion interpreta el formato de correos
		# electronicos del estandar RFC 822, que tiene letras, numeros y
		# algunos simbolos especiales, seguidos de un arroba, y luego el
		# formato de un dominio de internet.
		if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
			return True
		return False