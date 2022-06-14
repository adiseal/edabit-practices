# Author    : Adi Nugroho
# Date      : Jun/14/2022
# In this challenge you will be given three parameters, num1, num2, and an operator. Use the operator on number 1 and 2

def operate(num1, num2, operator):
	return eval(str(num1) + operator + str(num2))    

# print(operate(7, 10, "-")) ➞ -3