def one_list(lst):
	a = []
	for i in lst:
		for j in i:
			a = a + [j]
	return a
    
print(one_list([[True, False], [False, False]])) # [True, False, False, False]