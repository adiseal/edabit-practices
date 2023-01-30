def check_equality(a, b):
	return a == b and type(a) == type(b)
    
    
assert check_equality(1, true) == False
# A number and a boolean: the value and type are different.

assert check_equality(0, "0") == False
# A number and a string: the type is different.

assert check_equality(1,  1) == True
# A number and a number: the type and value are equal.