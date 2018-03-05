class Calculadora():

    # Criando um construtor
    def __init__(self,num1,num2):
        self.__num1 = num1
        self.__num2 = num2

    @property
    def num1(self):
        return self.__num1

    @property
    def num2(self):
    	return self.__num2


