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
        4) Longitud de 16 caracteres
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
        4) Longitud de 16 caracteres
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
        
######################### PARTICION 2: LOS USUARIOS No SE PUEDEN REGISTRAN error en formato de contrasena
######################### TIPO DE PRUEBA: FRONTERA

    # TAMANO DE CONTRASENA FRONTERA NO ACEPTADO 7 CARACTERES / 17 CARACTERES

    '''
    PRUEBA 7: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Exactamente 3 letras
        2) Exactamente 1 letra mayuscula
        3) Nuemero de digitos 4
        4) Longitud de 7 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''
    def test_frontera_registrarUsuarioP7(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjgf@gmail.com", "Maa5678","Maa5678"))
        self.assertFalse(self.seguridad.registrarUsuario("andres@gmail.com", "And5200","And5200"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafeix@gmail.com", "Myf5430","Myf5430"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco@gmail.com", "Ang0000","An00000"))
        self.assertFalse(self.seguridad.registrarUsuario("josegp@gmail.com", "1Mmj111","1Mmj111"))

    '''
    PRUEBA 8: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Exactamente 3 letras
        2) Exactamente una letra minuscula
        3) Nuemero de digitos 4 
        4) Longitud de 7 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''

    def test_frontera_registrarUsuarioP8(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjgf@gmail.com", "mAA5678","mAA5678"))
        self.assertFalse(self.seguridad.registrarUsuario("andres@gmail.com", "aND5200","aND5200"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafeix@gmail.com", "mYF5430","mYF5430"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco@gmail.com", "aNG0000","aNG0000"))
        self.assertFalse(self.seguridad.registrarUsuario("josegp@gmail.com", "11pMJ11","11pMJ11"))


    '''
    PRUEBA 9: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Numero de letras 6
        2) Exactamente un digito
        3) Numero de mayus/minus indeterminado 
        4) Longitud de 7 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''

    def test_frontera_registrarUsuarioP9(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjgf@gmail.com", "mAAaaa8","mAAaaa8"))
        self.assertFalse(self.seguridad.registrarUsuario("andres@gmail.com", "maNDmm0","maNDmm0"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafeix@gmail.com", "AmY1FFF","AmY1FFF"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco@gmail.com", "aNG0NGN","aNG0NGN"))
        self.assertFalse(self.seguridad.registrarUsuario("josegp@gmail.com", "1MpMJMJ","1MpMJMJ"))

    # LONGITUD EN FRONTERA INVALIDA DE CONTRASENA 17 CARACTERES
    '''
    PRUEBA 10: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Exactamente 3 letras
        2) Exactamente una letra mayuscula
        3) Nuemero de digitos 14 
        4) Longitud de 17 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''
    def test_frontera_registrarUsuarioP10(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjgf@gmail.com", "Maa15678111111111","Maa15678111111111"))
        self.assertFalse(self.seguridad.registrarUsuario("andres@gmail.com", "1And5200000000000","1And5200000000000"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0Myf5430000000000","0Myf5430000000000"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco@gmail.com", "Ang00000000000000","Ang00000000000000"))
        self.assertFalse(self.seguridad.registrarUsuario("josegp@gmail.com", "11Pmj111111111111","11Pmj111111111111"))

    '''
    PRUEBA 11: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Exactamente 3 letras
        2) Exactamente una letra minuscula
        3) Nuemero de digitos 14 
        4) Longitud de 17 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''

    def test_frontera_registrarUsuarioP11(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjgf@gmail.com", "mAA15678111111111","mAA15678111111111"))
        self.assertFalse(self.seguridad.registrarUsuario("andres@gmail.com", "1aND5200000000000","1aND5200000000000"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0mYF5430000000000","0mYF5430000000000"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco@gmail.com", "aNG00000000000000","aNG00000000000000"))
        self.assertFalse(self.seguridad.registrarUsuario("josegp@gmail.com", "11pMJ111111111111","11pMJ111111111111"))


    '''
    PRUEBA 12: Formato de contrasena
    Tipo: Frontera
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Numero de letras 16
        2) Exactamente un digito
        3) Numero de mayus/minus indeterminado 
        4) Longitud de 17 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''

    def test_frontera_registrarUsuarioP12(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjgf@gmail.com", "mmAAaaaa8aaaaaaaa","mmAAaaaa8aaaaaaaa"))
        self.assertFalse(self.seguridad.registrarUsuario("andres@gmail.com", "mmaNDmmm0mmmmmmmm","mmaNDmmm0mmmmmmmm"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafeix@gmail.com", "AmmY1FFFfmmmmmmmm","AmmY1FFFfmmmmmmmm"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco@gmail.com", "aNG0nNGNGaaaaaaaa","aNG0nNGNGaaaaaaaa"))
        self.assertFalse(self.seguridad.registrarUsuario("josegp@gmail.com", "1MpMJMJMppppppppp","1MpMJMJMppppppppp"))


    ################################# PRUEBAS DE ESQUINA
    ########################## PARTICION 1: los usuarios se registran satisfactoriamente

    # Tamano 8 y 16 caracteres y con tamano 7 y 17
    ##### PRUEBA 1 CON PRUEBA 3 
    ##### EXACTAMENTE 1 DIGITO
    ##### EXACTAMENTE UNA LETRA MAYUSCULA
    ##### AL MENOS 3 LETRAS

    ##### PRUEBA 2 CON PRUEBA 3
    ##### EXACTAMENTE 1 DIGITO
    ##### EXACRAMENTE UNA LETRA MINUSCULA
    ##### EXACTAMENTE 3 LETRAS

    ##### Con frontera 8 caracteres #####
    '''
    PRUEBA 13: Formato de contrasena
    Tipo: Esquina
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Al menos 3 letras
        2) Exactamente una letra mayuscula
        3) Nuemero de digitos 1 
        4) Longitud de 8 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''
    def test_esquina_registrarUsuarioP13(self):
        self.assertTrue(self.seguridad.registrarUsuario("mjgf@gmail.com", "Maaaaaa8","Maaaaaa8"))
        self.assertTrue(self.seguridad.registrarUsuario("andres@gmail.com", "1Anddddd","1Anddddd"))
        self.assertTrue(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0Myfffff","0Myfffff"))
        self.assertTrue(self.seguridad.registrarUsuario("angProco@gmail.com", "Ang0gggg","Ang0gggg"))
        self.assertTrue(self.seguridad.registrarUsuario("josegp@gmail.com", "1pPmjjjj","1pPmjjjj"))


    '''
    PRUEBA 14: Formato de contrasena
    Tipo: Esquina
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Al menos 3 letras
        2) Exactamente una letra minuscula
        3) Exactamente 1 digito 
        4) Longitud de 8 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''

    def test_esquina_registrarUsuarioP14(self):
        self.assertTrue(self.seguridad.registrarUsuario("mjgf@gmail.com", "mAA1AAAA","mAA1AAAA"))
        self.assertTrue(self.seguridad.registrarUsuario("andres@gmail.com", "1aNDDDDD","1aNDDDDD"))
        self.assertTrue(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0mYFFFFF","0mYFFFFF"))
        self.assertTrue(self.seguridad.registrarUsuario("angProco@gmail.com", "aNG0NNNN","aNG0NNNN"))
        self.assertTrue(self.seguridad.registrarUsuario("josegp@gmail.com", "1pMJMJMJ","1pMJMJMJ"))

##### CON FRONTERA 16 CARACTERES. RESULTADO ESPERADO: el usuario se registra satisfactoriamente #####

    ##### PRUEBA 4 CON PRUEBA 6 
    ##### EXACTAMENTE 1 DIGITO
    ##### EXACTAMENTE UNA LETRA MAYUSCULA
    ##### AL MENOS 3 LETRAS

    ##### PRUEBA 5 CON PRUEBA 6
    ##### EXACTAMENTE 1 DIGITO
    ##### EXACRAMENTE UNA LETRA MINUSCULA
    ##### AL MENOS 3 LETRAS

    '''
    PRUEBA 15: Formato de contrasena
    Tipo: Esquina
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Al menos 3 letras
        2) Exactamente una letra mayuscula
        3) Exactamente un digito 
        4) Longitud de 16 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''
    def test_esquina_registrarUsuarioP15(self):
        self.assertTrue(self.seguridad.registrarUsuario("mjgf@gmail.com", "Maa1aaaaaaaaaaaa","Maa1aaaaaaaaaaaa"))
        self.assertTrue(self.seguridad.registrarUsuario("andres@gmail.com", "1Anddddddddddddd","1Anddddddddddddd"))
        self.assertTrue(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0Myfffffffffffff","0Myfffffffffffff"))
        self.assertTrue(self.seguridad.registrarUsuario("angProco@gmail.com", "Ang0gggggggggggg","Ang0gggggggggggg"))
        self.assertTrue(self.seguridad.registrarUsuario("josegp@gmail.com", "1pPmjjjjjjjjjjjj","1pPmjjjjjjjjjjjj"))

    
    '''
    PRUEBA 16: Formato de contrasena
    Tipo: Esquina
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Al menos 3 letras
        2) Exactamente una letra minuscula
        3) Exactamente un digito 
        4) Longitud de 16 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''

    def test_esquina_registrarUsuarioP16(self):
        self.assertTrue(self.seguridad.registrarUsuario("mjgf@gmail.com", "mAA1AAAAAAAAAAAA","mAA1AAAAAAAAAAAA"))
        self.assertTrue(self.seguridad.registrarUsuario("andres@gmail.com", "1aNDDDDDDDDDDDDD","1aNDDDDDDDDDDDDD"))
        self.assertTrue(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0mYFFFFFFFFFFFFF","0mYFFFFFFFFFFFFF"))
        self.assertTrue(self.seguridad.registrarUsuario("angProco@gmail.com", "1aNGJJJJJJJJJJJJ","1aNGJJJJJJJJJJJJ"))
    

    ##### CON FRONTERA NO VALIDA CON 7 CARACTERES. RESULTADO ESPERADO: el usuario NO se registra satisfactoriamente #####

    ##### PRUEBA 7 CON PRUEBA 9 
    ##### EXACTAMENTE 1 DIGITO
    ##### EXACTAMENTE UNA LETRA MAYUSCULA
    ##### AL MENOS 3 LETRAS

    ##### PRUEBA 8 CON PRUEBA 9
    ##### EXACTAMENTE 1 DIGITO
    ##### EXACRAMENTE UNA LETRA MINUSCULA
    ##### AL MENOS 3 LETRAS



    '''
    PRUEBA 17: Formato de contrasena
    Tipo: Esquina
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Al menos 3 letras
        2) Exactamente 1 letra mayuscula
        3) Exactamente 1 digito
        4) Longitud de 7 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''
    def test_esquina_registrarUsuarioP17(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjgf@gmail.com", "Maaaaa8","Maaaaa8"))
        self.assertFalse(self.seguridad.registrarUsuario("andres@gmail.com", "Andddd5","Andddd5"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafeix@gmail.com", "Myffff0","Myffff0"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco@gmail.com", "Angggg0","Angggg0"))
        self.assertFalse(self.seguridad.registrarUsuario("josegp@gmail.com", "1Mmjjjj","1Mmjjjj"))


    '''
    PRUEBA 18: Formato de contrasena
    Tipo: Esquina
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Al menos 3 letras
        2) Exactamente una letra minuscula
        3) Exactamente un digito 
        4) Longitud de 7 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''

    def test_malicia_registrarUsuarioP18(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjgf@gmail.com", "mAA5AAA","mAA5AAA"))
        self.assertFalse(self.seguridad.registrarUsuario("andres@gmail.com", "aND5DDD","aND5DDD"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafeix@gmail.com", "mYF5FFF","mYF5FFF"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco@gmail.com", "aNG0GGG","aNG0GGG"))
        self.assertFalse(self.seguridad.registrarUsuario("josegp@gmail.com", "1ppMJMJ","1ppMJMJ"))

    
     ##### CON FRONTERA NO VALIDA CON 17 CARACTERES. RESULTADO ESPERADO: el usuario NO se registra satisfactoriamente #####

    ##### PRUEBA 10 CON PRUEBA 12 
    ##### EXACTAMENTE 1 DIGITO
    ##### EXACTAMENTE UNA LETRA MAYUSCULA
    ##### AL MENOS 3 LETRAS

    ##### PRUEBA 11 CON PRUEBA 12
    ##### EXACTAMENTE 1 DIGITO
    ##### EXACRAMENTE UNA LETRA MINUSCULA
    ##### AL MENOS 3 LETRAS

    '''
    PRUEBA 19: Formato de contrasena
    Tipo: Esquina
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Al menos 3 letras
        2) Exactamente una letra mayuscula
        3) Exactamente 1 digito 
        4) Longitud de 17 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''
    def test_esquina_registrarUsuarioP19(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjgf@gmail.com", "Maa1aaaaaaaaaaaaa","Maa1aaaaaaaaaaaaa"))
        self.assertFalse(self.seguridad.registrarUsuario("andres@gmail.com", "1Andddddddddddddd","1Andddddddddddddd"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0Myffffffffffffff","0Myffffffffffffff"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco@gmail.com", "Ang0ggggggggggggg","Ang0ggggggggggggg"))
        self.assertFalse(self.seguridad.registrarUsuario("josegp@gmail.com", "1pPmjjjjjjjjjjjjj","1pPmjjjjjjjjjjjjj"))


    '''
    PRUEBA 20: Formato de contrasena
    Tipo: Esquina
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que se registre el usuario de forma correcta con una contrasena
    con:
    Caracteristicas de contrasena:
        1) Al menos 3 letras
        2) Exactamente una letra minuscula
        3) Exactamente un digito 
        4) Longitud de 17 caracteres
    Caracteristicas de email:
        1) email cumple con RFC 822

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''

    def test_esquina_frontera_registrarUsuarioP20(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjgf@gmail.com", "mAA1AAAAAAAAAAAAA","mAA1AAAAAAAAAAAAA"))
        self.assertFalse(self.seguridad.registrarUsuario("andres@gmail.com", "1aNDDDDDDDDDDDDDD","1aNDDDDDDDDDDDDDD"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0mYFFFFFFFFFFFFFF","0mYFFFFFFFFFFFFFF"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco@gmail.com", "1aNGJJJJJJJJJJJJJ","1aNGJJJJJJJJJJJJJ"))



    ########################################### CASOS DE PRUEBA DE MALICIA ####################################


    ########### PRUEBA MALICIOSA: correo invalido ##############
    ########### PROBAMOS FUNCION registrarUsuario  ##############

    '''
    PRUEBA 21: Formato de correo
    Tipo: Malicia
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que el usuario que se registre use como correo alguno 
    que cumpla el formato RFC 822. En este caso: Falta de ., com y @

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''
    def test_malicia_registrarUsuarioP21(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjgf@gmail", "Maa15678","Maa15678"))
        self.assertFalse(self.seguridad.registrarUsuario("andrescom", "1And5200","1And5200"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafeixgmail.com", "0Myf5430","0Myf5430"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco@gmailcom", "Ang00000","Ang00000"))
        self.assertFalse(self.seguridad.registrarUsuario("josegp.com", "11Pmj111","11Pmj111"))


    '''
    PRUEBA 22: Formato de correo
    Tipo: Malicia
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que el usuario que se registre use como correo alguno 
    que cumpla el formato RFC 822. En este caso: caracteres especiales no aceptados

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''
    def test_malicia_registrarUsuarioP22(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjg##f@gmail.com", "Maa15678","Maa15678"))
        self.assertFalse(self.seguridad.registrarUsuario("andr%%%es@gmail.com", "1And5200","1And5200"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafe^ix@gmail.com", "0Myf5430","0Myf5430"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco&&&@gmail.com", "Ang00000","Ang00000"))
        self.assertFalse(self.seguridad.registrarUsuario("joseg$$$p@gmail.com", "11Pmj111","11Pmj111"))

    '''
    PRUEBA 23: Formato de contrasena
    Tipo: Malicia
    Funcion a probar: registrarUsuario en seguridad.py
    Descripcion del caso: se pone a prueba que el usuario que se registre use una contrasena
    aceptada por el mecanismo de seguridad. En este caso: caracteres especiales (que no son
    aceptados)

    Resultado de la prueba: el usuario se registra satisfactoriamente
    '''
    def test_malicia_registrarUsuarioP23(self):
        self.assertFalse(self.seguridad.registrarUsuario("mjgf@gmail.com", "Maa$$15678","Maa$$15678"))
        self.assertFalse(self.seguridad.registrarUsuario("andres@gmail.com", "1And5200###","1And5200###"))
        self.assertFalse(self.seguridad.registrarUsuario("mariafeix@gmail.com", "0Myf5430&","0Myf5430&"))
        self.assertFalse(self.seguridad.registrarUsuario("angProco@gmail.com", "Ang*00000","Ang*00000"))
        self.assertFalse(self.seguridad.registrarUsuario("josegp@gmail.com", "11Pmj1!!11","11Pmj1!!11"))

       
    
    ########### PRUEBA MALICIOSA: clave de registro invalida ##############
    ########### PROBAMOS FUNCION registrarUsuario  ##############




if __name__ == '__main__':
	unittest.main()