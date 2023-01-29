def variable_valid(var):
	return var.isidentifier()
    
    
assert variable_valid("result") == True

assert variable_valid("odd_nums") == True

assert variable_valid("2TimesN") == False