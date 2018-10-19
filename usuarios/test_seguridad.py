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

######################### PARTICION 1: LOS USUARIOS SE REGISTRAN SATISFACTORIAMENTE
######################### TIPO DE PRUEBA: FRONTERA
    
    # FRONTERA MINIMA DE LONGITUD ACEPTABLE: 8 CARACTERES
    '''
    PRUEBA 1: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Exactamente 3 letras
        2) Exactamente una letra mayuscula
        3) Nuemero de digitos 5 
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
        3) Nuemero de digitos 5 
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

    '''
    PRUEBA 3: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Numero de letras 7
        2) Exactamente un digito
        3) Numero de mayus/minus indeterminado 
        4) Longitud de 8 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''

    def test_frontera_registrarUsuarioP3(self):
        self.assertTrue(self.seguridad.registrarUsuario("mjgf@gmail.com", "mAAaaaa8","mAAaaaa8"))
        self.assertTrue(self.seguridad.registrarUsuario("andres@gmail.com", "maNDmmm0","maNDmmm0"))
        self.assertTrue(self.seguridad.registrarUsuario("mariafeix@gmail.com", "AmY1FFFf","AmY1FFFf"))
        self.assertTrue(self.seguridad.registrarUsuario("angProco@gmail.com", "aNG0NGNG","aNG0NGNG"))
        self.assertTrue(self.seguridad.registrarUsuario("josegp@gmail.com", "1MpMJMJM","1MpMJMJM"))
        
    # FRONTERA MAXIMA DE LONGITUD ACEPTABLE: 16 CARACTERES
    '''
    PRUEBA 4: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Exactamente 3 letras
        2) Exactamente una letra mayuscula
        3) Nuemero de digitos 13 
        4) Longitud de 16 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''
    def test_frontera_registrarUsuarioP4(self):
        self.assertTrue(self.seguridad.registrarUsuario("mjgf@gmail.com", "Maa1567811111111","Maa1567811111111"))
        self.assertTrue(self.seguridad.registrarUsuario("andres@gmail.com", "1And520000000000","1And520000000000"))
        self.assertTrue(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0Myf543000000000","0Myf543000000000"))
        self.assertTrue(self.seguridad.registrarUsuario("angProco@gmail.com", "Ang0000000000000","Ang0000000000000"))
        self.assertTrue(self.seguridad.registrarUsuario("josegp@gmail.com", "11Pmj11111111111","11Pmj11111111111"))

    '''
    PRUEBA 5: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Exactamente 3 letras
        2) Exactamente una letra minuscula
        3) Nuemero de digitos 13 
        4) Longitud de 8 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''

    def test_frontera_registrarUsuarioP5(self):
        self.assertTrue(self.seguridad.registrarUsuario("mjgf@gmail.com", "mAA1567811111111","mAA1567811111111"))
        self.assertTrue(self.seguridad.registrarUsuario("andres@gmail.com", "1aND520000000000","1aND520000000000"))
        self.assertTrue(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0mYF543000000000","0mYF543000000000"))
        self.assertTrue(self.seguridad.registrarUsuario("angProco@gmail.com", "aNG0000000000000","aNG0000000000000"))
        self.assertTrue(self.seguridad.registrarUsuario("josegp@gmail.com", "11pMJ11111111111","11pMJ11111111111"))

    '''
    PRUEBA 6: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Numero de letras 15
        2) Exactamente un digito
        3) Numero de mayus/minus indeterminado 
        4) Longitud de 8 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''

    def test_frontera_registrarUsuarioP6(self):
        self.assertTrue(self.seguridad.registrarUsuario("mjgf@gmail.com", "mAAaaaa8aaaaaaaa","mAAaaaa8aaaaaaaa"))
        self.assertTrue(self.seguridad.registrarUsuario("andres@gmail.com", "maNDmmm0mmmmmmmm","maNDmmm0mmmmmmmm"))
        self.assertTrue(self.seguridad.registrarUsuario("mariafeix@gmail.com", "AmY1FFFfmmmmmmmm","AmY1FFFfmmmmmmmm"))
        self.assertTrue(self.seguridad.registrarUsuario("angProco@gmail.com", "aNG0NGNGaaaaaaaa","aNG0NGNGaaaaaaaa"))
        self.assertTrue(self.seguridad.registrarUsuario("josegp@gmail.com", "1MpMJMJMpppppppp","1MpMJMJMpppppppp"))
        
if __name__ == '__main__':
	unittest.main()