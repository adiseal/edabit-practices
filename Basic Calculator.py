def calculator(num1, operator, num2):
	if num2 == 0:
		return "Can't divide by 0!"
	elif operator == "+":
		return num1 + num2
	elif operator == "-":
		return num1 - num2
	elif operator == "/":
		return num1 / num2
	elif operator == "*":
		return num1 * num2
	