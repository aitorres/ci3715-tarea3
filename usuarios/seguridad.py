import re # Se importa este modulo para verificar expresiones regulares

'''
La clase Seguridad esta construida para permitir el registro
y la autenticacion de los usuarios siguiendo algunas reglas de seguridad.
'''
class Seguridad:

	def __init__(self):
		'''
		Constructor del modulo Seguridad. Con cada instancia se inicializan
		estos valores y, si se necesitan cambiar, se pueden hacer rapidamente
		en este segmento. Asi se reduce a cero la necesidad de tener constantes
		magicas en el codigo.
		'''

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
		'''
		Dado un correo electronico y dos claves candidatas, verifica que
		el correo sea valido segun un correo, y que las claves sean validas
		segun criterios como claves iguales, letras minimas y digitos minimos.
		'''

		if self.es_correo_valido(email) and self.es_clave_valida(clave1, clave2):
			# Hacemos reverse de la clave con metodos de string slicing
			self.usuarios[email] = clave1[::-1]
			return True

		return False

	def ingresarUsuario(self, email, clave):
		'''
		Determina si un email y clave son validos y estan registrados
		para hacer login.
		'''
		if not (self.es_correo_valido(email) and self.es_clave_valida(clave, clave)):
			return False

		return self.esta_en_diccionario(email, clave)

	def esta_en_diccionario(self, email, clave):
		'''
		Verifica si un par de correo y clave esta en el diccionario de la instancia.
		'''
		clave_reversa = clave[::-1]

		try:
			return (self.usuarios[email] == clave_reversa)
		except KeyError:
			return False

	def es_correo_valido(self, email):
		'''
		Verifica si un correo esta en el formato valido.
		'''

		# El regex a continuacion interpreta el formato de correos
		# electronicos del estandar RFC 822, que tiene letras, numeros y
		# algunos simbolos especiales, seguidos de un arroba, y luego el
		# formato de un dominio de internet.
		if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
			return True
		return False

	def es_clave_valida(self, clave1, clave2):
		'''
		Verifica si una clave o un par de claves pasan todas las pruebas de validez.
		'''

		# Claves coinciden entre si
		if not self.claves_coinciden(clave1, clave2):
			return False

		# Clave entre minimo y maximo
		if not self.clave_tiene_longitud_correcta(clave1):
			return False

		# Clave solo con los simbolos permitidos
		if not self.clave_tiene_simbolos_permitidos(clave1):
			return False

		# Claves con la cantidad de letras minimas
		if not self.clave_tiene_letras_minimas(clave1):
			return False

		# Claves con la cantidad de digitos minimos
		if not self.clave_tiene_digitos_minimos(clave1):
			return False

		return True

	def claves_coinciden(self, clave1, clave2):
		'''
		Verifica si dos claves coinciden.
		'''

		return clave1 == clave2

	def clave_tiene_longitud_correcta(self, clave):
		'''
		Verifica si una clave esta entre el minimo
		y el maximo en longitud.
		'''

		tamano_clave = len(clave)
		return (self.longitud_minima <= tamano_clave) and (tamano_clave <= self.longitud_maxima)

	def clave_tiene_simbolos_permitidos(self, clave):
		'''
		Verifica si una clave tiene solo los simbolso permitidos
		'''

		# Solo se permiten letras mayusculas, minusculas
		# y numeros
		if re.match(r"^[a-zA-Z0-9]+$", clave):
			return True
		return False

	def clave_tiene_letras_minimas(self, clave):
		'''
		 Cuenta en una clave las letras y verifica que cumpla
		 con la cantidad minima.
		'''

		letras, mayusculas, minusculas = 0, 0, 0

		for letra in clave:
			# Cuenta letras en general
			if re.match(r"^[a-zA-Z]", letra):
				letras +=1

			# Cuenta letras minusculas
			if re.match(r"^[a-z]", letra):
				minusculas += 1

			# Cuenta letras mayusculas
			if re.match(r"^[A-Z]", letra):
				mayusculas += 1

			if letras >= self.letras_minimas and mayusculas >= self.mayusculas_minimas and minusculas >= self.minusculas_minimas:
				return True

		return False

	def clave_tiene_digitos_minimos(self, clave):
		'''
		 Cuenta en una clave los digitos y verifica que cumpla
		 con la cantidad minima.
		'''
		digitos = 0

		for caracter in clave:
			# Cuenta los digitos
			if re.match(r"^[0-9]", caracter):
				digitos += 1

			if digitos >= self.digitos_minimos:
				return True

		return False
