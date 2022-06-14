# Author    : Adi Nugroho
# Date      : Jun/14/2022
# a function that takes two numbers and a mathematical operator and returns the result

def calculate(num1, num2, op):
    return eval(str(num1) + op + str(num2))

# print(calculate(25, 5, "//")) ➞ 5
# print(calculate(14, 3, "%"))  ➞ 2