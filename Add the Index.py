def add_indexes(lst):
	a = []
	count = -1
	for i in lst:
		count = count + 1
		a = a + [count + i]
	return a
	
print(add_indexes([5, 4, 3, 2, 1])) # [5, 5, 5, 5, 5]
print(add_indexes([0, 0, 0, 0, 0])) # [0, 1, 2, 3, 4]
print(add_indexes([5, 4, 3, 2, 1])) # [5, 5, 5, 5, 5]
print(add_indexes([-25, -15, 3])) # [-25, -14, 5]
print(add_indexes([27])) # [27]
print(add_indexes([-48, -20, 41, 29, -25, -17, -13, 5, 4, -5, 3, -17, 23])) # [-48, -19, 43, 32, -21, -12, -7, 12, 12, 4, 13, -6, 35]   