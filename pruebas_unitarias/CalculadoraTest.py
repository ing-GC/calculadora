import unittest
from Calculadora import Calculadora
class CalculadoraTest(unittest.TestCase):
	def test_valor_de_inicio_igual_a_cero(self):
		calc=Calculadora()
		self.assertEquals(calc.obtener_resultado(),0)

	def test_sumar_2_mas_2_igual_4(self):
		calc=Calculadora()
		calc.suma(2,2)
		self.assertEquals(calc.obtener_resultado(),4)
	
	def test_sumar_3_mas_3_igual_6(self):
		calc=Calculadora()
		calc.suma(3,3)
		self.assertEquals(calc.obtener_resultado(),6)

	def test_sumar_menos1_mas_2_igual_1(self):
		calc=Calculadora()
		calc.suma(-1,2)
		self.assertEquals(calc.obtener_resultado(),1)
	def test_sumar_l_mas_2_igual_error(self):
		calc=Calculadora()
		calc.suma('l',2)
		self.assertEquals(calc.obtener_resultado(),'Datos incorrectos')

	def test_restar_9_menos_3_igual_6(self):
		calc=Calculadora()
		calc.resta(9,3)
		self.assertEquals(calc.obtener_resultado(),6)	
	def test_multiplicar_7_por_8_56(self):
		calc=Calculadora()
		calc.multiplicacion(7,8)
		self.assertEquals(calc.obtener_resultado(),56)
	def test_dividir_8_2_4(self):
		calc=Calculadora()
		calc.division(8,2)
		self.assertEquals(calc.obtener_resultado(),4)

	def test_potencia_3_3_27(self):
		calc=Calculadora()
		calc.potencia(3,3)
		self.assertEquals(calc.obtener_resultado(),27)

	def test_raiz_25_5(self):
		calc=Calculadora()
		calc.raiz(25)
		self.assertEquals(calc.obtener_resultado(),5)

	def test_raiz_menos25_5(self):
		calc=Calculadora()
		calc.raiz(-25)
		self.assertEquals(calc.obtener_resultado(),'Solo numeros reales')




if __name__ == '__main__':
	unittest.main()