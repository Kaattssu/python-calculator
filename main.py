def sumar():
	x = a + b
	print (("Resultado:"), (x))
def restar():
	x = a - b
	print (("Resultado:"), (x))
def multiplicar():
	x = a * b
	print (("Resultado:"), (x))
def dividir():
	x = a / b
	print (("Resultado:"), (x))

while True:
	try:
		a = int(input("Ingresa el primer numero: \n"))
		b = int(input("Ingresa el segundo numero: \n"))
		print (("Que calculo quieres realizar entre"), (a), ("y"), (b), ("?\n"))
		op = str(input("""
		1- sumar
		2- restar
		3- multiplicar
		4- dividir \n"""))
	except:
		print("Error")
		op = '?'
	if op == '1':
		sumar()
		break
	elif op == '2':
		restar()
		break
	elif op == '3':
		multiplicar()
		break
	elif op == '4':
		dividir()
		break
	else:
		print ("¡Has ingresado un numero incorrecto!")
