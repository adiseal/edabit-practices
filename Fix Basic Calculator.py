def basic_calculator(a, o, b):
    result = None
    # a = 1, b = 0, o = "/"
    if(o == "+"):
        return a + b
    elif(o == "-"):
        return a - b
    elif(o == "/" and b != 0):
        return a / b
    elif(o == "*"):
        return a * b
    return result
    
    
print(basic_calculator(3,"*",4))
assert basic_calculator(2, '+',  4) == 6

assert basic_calculator(6, '-', 5) == 1

assert basic_calculator(12, '/', 3) == 4

assert basic_calculator(3, '*', 4) == 12
assert basic_calculator(1, '/', 0) == None
# Division by zero is not possible

assert basic_calculator(1, 'x', 0) == None
# 'x' is not an operator