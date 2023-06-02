def multiply(l):
	b = []
	a = len(l)
	for i in l:
		b += [[i]*a]
	return b
	
print(multiply([4, 5])) # [[4, 4], [5, 5]]