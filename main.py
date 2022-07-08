def sumar():
	x = a + b
	print (("Result:"), (x))
def restar():
	x = a - b
	print (("Result:"), (x))
def multiplicar():
	x = a * b
	print (("Result:"), (x))
def dividir():
	x = a / b
	print (("Result:"), (x))

while True:
	try:
		a = int(input("Enter the first number: \n"))
		b = int(input("Enter the second number: \n"))
		print (("What calc do you want to do?"), (a), ("y"), (b), ("?\n"))
		op = str(input("""
		1- Add
		2- Subtract
		3- Multiply
		4- Split \n"""))
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
			print ("That's a wrong number!")
	except:
		print("Error")
		op = '?'

