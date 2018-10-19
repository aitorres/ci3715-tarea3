# encoding=utf-8
from django.test import TestCase

# Se importa el modulo de PyUnit para realizar las
# pruebas unitarias
import unittest
from seguridad import Seguridad

# AGREGANDO CASOS DE PRUEBA: FRONTERA, MALICIA Y MALICIA

class TestSeguridad(unittest.TestCase):

    def setUp(self):
        self.seguridad = Seguridad()
        
    def tearDown(self):
        self.seguridad = None

    
    '''
    PRUEBA 1: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Exactamente 3 letras
        2) Exactamente una letra mayuscula
        3) Nuemero de digitos indeterminado 
        4) Longitud de 8 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''
    def test_frontera_registrarUsuarioP1(self):
        self.assertTrue(self.seguridad.registrarUsuario("mjgf@gmail.com", "Maa15678","Maa15678"))
        self.assertTrue(self.seguridad.registrarUsuario("andres@gmail.com", "1And5200","1And5200"))
        self.assertTrue(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0Myf5430","0Myf5430"))
        self.assertTrue(self.seguridad.registrarUsuario("angProco@gmail.com", "Ang00000","Ang00000"))
        self.assertTrue(self.seguridad.registrarUsuario("josegp@gmail.com", "11Pmj111","11Pmj111"))

    '''
    PRUEBA 2: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Exactamente 3 letras
        2) Exactamente una letra minuscula
        3) Nuemero de digitos indeterminado 
        4) Longitud de 8 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''

    def test_frontera_registrarUsuarioP2(self):
        self.assertTrue(self.seguridad.registrarUsuario("mjgf@gmail.com", "mAA15678","mAA15678"))
        self.assertTrue(self.seguridad.registrarUsuario("andres@gmail.com", "1aND5200","1aND5200"))
        self.assertTrue(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0mYF5430","0mYF5430"))
        self.assertTrue(self.seguridad.registrarUsuario("angProco@gmail.com", "aNG00000","aNG00000"))
        self.assertTrue(self.seguridad.registrarUsuario("josegp@gmail.com", "11pMJ111","11pMJ111"))

if __name__ == '__main__':
	unittest.main()