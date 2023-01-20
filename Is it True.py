def is_it_true(relation):
	return eval(relation.replace("=", "=="))

    
assert is_it_true("2=2") == True

assert is_it_true("8<7") == False

assert is_it_true("5=13") == False

assert is_it_true("15>4") == True