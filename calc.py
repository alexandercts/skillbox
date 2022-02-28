x = input("Выберите операцию: ")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if x == "+":
	print("a + b =", a + b)
elif x == "-":
	print("a - b =", a - b)
elif x == "*":
	print("a * b =", a * b)
elif x == "/":
	if b == 0:
		print("Ошибка! На ноль делить нельзя!")
	else:
		print("a / b =", a / b)
else:
	print("Ошибка: такой операции не существует. Попробуйте ещё раз.")