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
print(add_indexes([-32, -24, -50, 48, 5, -27, -33, -3, 16, -16, -31, -11, 43])) # [-32, -23, -48, 51, 9, -22, -27, 4, 24, -7, -21, 0, 55]
print(add_indexes([38, -8, 40, -50, -26, -3, -29, -33, 13, 28])) # [38, -7, 42, -47, -22, 2, -23, -26, 21, 37]