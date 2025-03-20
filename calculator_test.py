import unittest 
import calculator

def test_div_str(self):
    """
    La division de douze par deux ne doit rien retourner.
    """
    self.assertIsNone(calculator.divide("douze","deux"))

def test_div(self):
    """
    La division de 12 par 2 doit retourner 6.
    """
    self.assertEqual(calculator.divide("12","2"),6)

def test_div_zero(self):
    """
    Une division par 0.
    """
    self.assertIsNone(calculator.divide("2","0"))  

def test_mult(self):
    """
    La multiplication de 13 par 13 doit retourner 169.
    """
    self.assertEqual(calc.mult("13","13"),169)

def test_mult_str(self):
    """
    La multiplication entre mult et 18 ne doit rien retourner.
    """
    self.assertIsNone(calc.mult("mult","18"))

def test_mult_float(self):
    """
    La multiplication entre 2 float ne doit rien retourner.
    """
    self.assertIsNone(calc.sous("0.5","2.8"))

def test_ope(self):
    """        
    La soustraction entre 12 et 2 doit retourner 10.
    """
    self.assertEqual(calculator.substract("12","2"),10)    

def test_ope_erreur(self):
    """
    L'opérateur factoriel n'est pas pris en compte.
    """
    self.assertIsNone(calculator.ope("!","2","3")) 

def test_coucou():
    # Fonction test si la résultat renvoie 'hello'
    output = 'hello'
    assert output == 'hello'

def test_add_str(self):
    """
    L'addition entre 2 et add ne doit rien retourner.
    """
    self.assertIsNone(calculator.add("2","add"))