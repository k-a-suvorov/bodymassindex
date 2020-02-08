#Console boody mass index program 1.0

try:
	print('Расчитайите свой индекс массы тела. \tМасса вашего тела =')
	a = float(input('Ваш вес = '))
	print('Рост в сантиметрах = ')
	b = float(input('Ваш рост = '))
	height = b / 100
	result = round(a /height**2, 2)

	if (result <= 24.9):
		print(f'У вас нормальная масса тела - {result}')
	elif (result <= 29.9):
		print(f'У вас повышенная  масса тела - {result}')
	elif (result <= 34.9):
		print(f'У вас Ожирение первой степени - {result}')
	elif (result <= 39.9):
		print(f'У вас ожирение второй степени - {result}')
	else:
		print(f'У вас ожирение третьей степени - {result}')
except ValueError:
    print('Next time, please insert correct integer numbers')
except TypeError:
    print("You have some mistake of userinput Value!")
