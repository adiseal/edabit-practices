def transform(lst):
	a = []
	for i in lst:
		if i % 2 == 0:
			a = a + [i-1]
		else:
			a = a + [i+1]
	return a
    
print(transform([3, 3, 4, 3])) # [4, 4, 3, 4]