from contas import Soma, Exponenciacao

class RealizaCalculo():

 	def realiza_calculo(self, num1, num2, operacao):
 		calculo = operacao.calcular(num1,num2)
 		print (calculo)
 		
if __name__ == '__main__':
	
	from calculadora import Calculadora

	calculador = RealizaCalculo()
	valores = Calculadora(2,4)

	calculador.realiza_calculo(valores.num1, valores.num2, Soma())
	calculador.realiza_calculo(valores.num1, valores.num2, Exponenciacao())

