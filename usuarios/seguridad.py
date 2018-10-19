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

		# Requisitos de letras minimas en claves
		self.letras_minimas = 3
		self.mayusculas_minimas = 1
		self.minusculas_minimas = 1

		# Requisitos de digitos minimos en claves
		self.digitos_minimos = 1

		# Diccionario de usuarios
		self.usuarios = dict()

	def registrarUsuario(self, email, clave1, clave2):
		if self.es_correo_valido(email) and self.es_clave_valida(clave1, clave2):
			# Hacemos reverse de la clave con metodos de string slicing
			self.usuarios[email] = clave1[::-1]
			return True

		return False

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

		if not self.clave_tiene_longitud_correcta(clave1):
			return False

		if not self.clave_tiene_simbolos_permitidos(clave1):
			return False

		if not self.clave_tiene_letras_minimas(clave1):
			return False

		if not self.clave_tiene_digitos_minimos(clave1):
			return False

		return True 

	def claves_coinciden(self, clave1, clave2):
		return clave1 == clave2

	def clave_tiene_longitud_correcta(self, clave):
		tamano_clave = len(clave)
		return (self.longitud_minima <= tamano_clave) and (tamano_clave <= self.longitud_maxima)

	def clave_tiene_simbolos_permitidos(self, clave):
		# Solo se permiten letras mayusculas, minusculas
		# y numeros
		if re.match(r"^[a-zA-Z0-9]+$", clave):
			return True
		return False

	def clave_tiene_letras_minimas(self, clave):
		letras, mayusculas, minusculas = 0, 0, 0

		for letra in clave:
			if re.match(r"^[a-zA-Z]", letra):
				letras +=1

			if re.match(r"^[a-z]", letra):
				minusculas += 1

			if re.match(r"^[A-Z]", letra):
				mayusculas += 1

			if letras >= self.letras_minimas and mayusculas >= self.mayusculas_minimas and minusculas >= self.minusculas_minimas:
				return True

		return False

	def clave_tiene_digitos_minimos(self, clave):
		digitos = 0

		for caracter in clave:
			if re.match(r"^[0-9]", caracter):
				digitos += 1

			if digitos >= self.digitos_minimos:
				return True

		return False

