def integer_boolean(n):
	a = []
	for i in n:
		if i == "1":
			a = a + [True]
		else:
			a = a + [False]
	return a
    
print(integer_boolean("100101")) # [True, False, False, True, False, True]