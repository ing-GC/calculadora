import math
class Calculadora():
	def  __init__(self):
		self.resultado=0

	def obtener_resultado(self):
		return self.resultado


	def suma(self,num1,num2):
		try:
			self.resultado=num1+num2
		except:
			self.resultado= 'Datos incorrectos'

	def resta(self,num1,num2):
		try:
			self.resultado=num1-num2
		except:
			self.resultado='Datos incorrectos'

	def multiplicacion(self,num1,num2):
		try:
			self.resultado=num1*num2	
		except:
			self.resultado='Datos incorrectos'
	def division(self,num1,num2):
		try:
			if(num2>0):
				self.resultado=num1/num2
			else:
				self.resultado='indefinido'
		except:
			self.resultado='Datos incorrectos'

	def potencia(self,num1,num2):
		try:
			self.resultado=pow(num1,num2)
		except:
			self.resultado='Datos incorrectos'

	def raiz(self,num1):
		try:
			if(num1>0):
				self.resultado=math.sqrt(num1)
			else:
				self.resultado='Solo numeros reales'
		except:
			self.resultado='Datos incorrectos'
