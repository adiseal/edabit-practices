def return_only_integer(lst):
	a= []
	for i in lst:
		if type(i) == int:
			a = a + [i]
	return a
    
print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"])) # [10, 56, 20, 3]