import pytest
import unittest

def test_suma_enteros():
    x = 3
    y = 6
    resultado = 9
    assert x+y == resultado


def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return (a/b) if (b>0) else 0

def elevarNumero(base, exponente):
    return base**exponente


#TEST UNITARIOS CON PYTEST

def test_suma():
    x=3
    y=4
    resultado = 7
    assert resultado == suma(x,y)

def test_resta():
    x= 10
    y= 5
    resultado = 5
    assert resultado == resta(x,y)


def test_multiplicacion():
    x= 10
    y= 10
    resultado = 100
    assert resultado == multiplicacion(x,y)

def test_division():
    x= 10
    y= 2
    resultado = 5
    assert resultado == division(x,y)

def test_elevar():
    base= 5
    exponente= 4
    resultado = 625
    assert resultado == elevarNumero(base, exponente)


#TEST UNITARIOS CON UNITTEST

class test(unittest. TestCase):
    def test_suma(self):
        self.assertAlmostEquals(suma(8,10),18)
    def test_resta(self):
        self.assertAlmostEquals(resta(18,10),8)
    def test_multiplicacion(self):
        self.assertAlmostEquals(multiplicacion(2,2),4)
    def test_division(self):
        self.assertAlmostEquals(division(8,2),4)
    def test_elevar(self):
        self.assertAlmostEquals(elevarNumero(2,2),4)


if __name__ == '__main__':
    unittest.main()