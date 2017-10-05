Feature: Operaciones de la calculadora
	Como usuario de la calculadora
	deseo realizar las distintas operaciones con la calculadora
	para obtener el resultado preciso de cada una de ellas 

	Scenario: Suma de 2 mas 2
		Dado que ingreso los numeros para sumar "2" y "2"
		cuando realizo la operación
		entonces obtengo el resultado "4"

	Scenario: Suma de 7 mas 5
		Dado que ingreso los numeros para sumar "7" y "5"
		cuando realizo la operación
		entonces obtengo el resultado "12"

	Scenario: Suma de 0 mas -7
		Dado que ingreso los numeros para sumar "0" y "-7"
		cuando realizo la operación
		entonces obtengo el resultado "-7"

	Scenario: Resta de 2 menos 2
		Dado que ingreso los numeros para restar "7" y "2"
		cuando realizo la operación
		entonces obtengo el resultado "5"

	Scenario: Resta de 7 menos 5
		Dado que ingreso los numeros para restar "10" y "9"
		cuando realizo la operación
		entonces obtengo el resultado "1"

	Scenario: Resta de 20 mas 7
		Dado que ingreso los numeros para restar "20" y "7"
		cuando realizo la operación
		entonces obtengo el resultado "13"

	Scenario: Multiplicacion de 2 por 10
		Dado que ingreso los numeros para multiplicar "2" y "10"
		cuando realizo la operación
		entonces obtengo el resultado "20"

	Scenario: Multiplicacion de 9 por 7
		Dado que ingreso los numeros para multiplicar "9" y "7"
		cuando realizo la operación
		entonces obtengo el resultado "63"

	Scenario: Multiplicacion de 11 por 7
		Dado que ingreso los numeros para multiplicar "11" y "7"
		cuando realizo la operación
		entonces obtengo el resultado "77"

	Scenario: Division de 80 entre 10
		Dado que ingreso los numeros para dividir "80" y "10"
		cuando realizo la operación
		entonces obtengo el resultado "8"

	Scenario: Division de 20 entre 4
		Dado que ingreso los numeros para dividir "20" y "4"
		cuando realizo la operación
		entonces obtengo el resultado "5"		

	Scenario: Division de 8 entre 4
		Dado que ingreso los numeros para dividir "8" y "4"
		cuando realizo la operación
		entonces obtengo el resultado "2"

	Scenario: Potencia de 2 a la 3
		Dado que ingreso los numeros para elevar a una potencia "2" y "3"
		cuando realizo la operación
		entonces obtengo el resultado "8"				

	Scenario: Potencia de 3 a la 3
		Dado que ingreso los numeros para elevar a una potencia "3" y "3"
		cuando realizo la operación
		entonces obtengo el resultado "27"				

	Scenario: Potencia de 5 a la 3
		Dado que ingreso los numeros para elevar a una potencia "5" y "3"
		cuando realizo la operación
		entonces obtengo el resultado "125"	

	Scenario: Raiz de 25
		Dado que ingreso el numero para obtener su raiz  "25" 
		cuando realizo la operación
		entonces obtengo el resultado "5"

	Scenario: Raiz de 9
		Dado que ingreso el numero para obtener su raiz  "9" 
		cuando realizo la operación
		entonces obtengo el resultado "3"
									


	