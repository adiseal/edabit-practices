def list_of_multiples (num, length):
	a = []
	for i in range(1,length+1):
		a += [num*i]
	return a
    
print(list_of_multiples(12, 10)) # [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]