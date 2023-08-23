import NumerosComplejos as lc
import unittest
import math
class TestCplxOperatins(unittest.TestCase):

    def test_suma(self):
        suma = lc.suma((3,5),(-2.6,6.8))
        self.assertAlmostEqual(suma[0],0.4)
        self.assertAlmostEqual(suma[1],11.8)
        suma = lc.suma((1,1),(1,1))
        self.assertAlmostEqual(suma[0],2)
        self.assertAlmostEqual(suma[1],2)   

    def test_producto(self):
        producto = lc.producto((3,5),(-2.6,6.8))
        self.assertAlmostEqual(producto[0],32.68)
        self.assertAlmostEqual(producto[1],7.4)
        producto = lc.producto((3,1),(-1,4))
        self.assertAlmostEqual(producto[0],7)
        self.assertAlmostEqual(producto[1],11)
    
    def test_resta(self):
        resta = lc.resta((1,1),(1,1))
        self.assertAlmostEqual(resta[0],0)
        self.assertAlmostEqual(resta[1],0)
        resta = lc.resta((2,1),(2,1))
        self.assertAlmostEqual(resta[0],1)
        self.assertAlmostEqual(resta[1],1)

    def test_dividir(self):
        dividir = lc.dividir((3,5),(-2.6,6.8))
        self.assertAlmostEqual(dividir[0],-0.037619314991577765)
        self.assertAlmostEqual(dividir[1],-0.46883773161145426)
        dividir = lc.dividir((3,-1),(2,2))
        self.assertAlmostEqual(dividir[0],0.2)
        self.assertAlmostEqual(dividir[1],-1.6)

    def test_modulo(self):
        modulo = lc.modulo(3,-2.6)
        self.assertAlmostEqual(modulo,3.9698866482558417)
        modulo = lc.modulo(1,1)
        self.assertAlmostEqual(modulo,1.414213562)

    def test_conjugado(self):
        conjugado = lc.conjugado(3,-2.6)
        self.assertAlmostEqual(conjugado,(3,2.6))
        conjugado = lc.conjugado(3,2.6)
        self.assertAlmostEqual(conjugado,(3,-2.6))
    
    def test_conversion_polar(self):
        conversion_polar = lc.conversion_polar(-1,1)
        self.assertAlmostEqual(conversion_polar,(1.4142135623730951, -0.7853981633974483))
        conversion_polar = lc.conversion_polar(3,9)
        self.assertAlmostEqual(conversion_polar,(9.486832980505138, 1.2490457723982544))

    def test_conversion_cartesiana(self):
        conversion_cartesiana = lc.conversion_cartesiana(2,math.pi / 4)
        self.assertAlmostEqual(conversion_cartesiana,(1.4142135623730951,1.4142135623730951))
        conversion_cartesiana = lc.conversion_cartesiana(2,math.pi / 6)
        self.assertAlmostEqual(conversion_cartesiana,(1.7320508075688774,0.9999999999999999))

    def test_fase_numero_complejo(self):
        fase_numero_complejo = lc.fase_numero_complejo(-1,1)
        self.assertAlmostEqual(fase_numero_complejo,(-0.7853981633974483))
        fase_numero_complejo = lc.fase_numero_complejo(3,9)
        self.assertAlmostEqual(fase_numero_complejo,(0.3217505543966422))


if __name__ == "__main__":
    unittest.main()