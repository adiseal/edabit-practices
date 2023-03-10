def arithmetic_progression(start, diff, n):
	a = [str(start)]
	for i in range(1,n):
		start = start + diff
		a.append(str(start))
	return ", ".join(a)
    
print(arithmetic_progression(1, -3, 10)) # "1, -2, -5, -8, -11, -14, -17, -20, -23, -26"