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
print(add_indexes([-1, -3, -20, 13, 19, -12, 15, 8, -49, 27, -21, 17, 41, 17, 5, -45, -33])) # [-1, -2, -18, 16, 23, -7, 21, 15, -41, 36, -11, 28, 53, 30, 19, -30, -17]
print(add_indexes([35, -48, -17, 25, 25, -45, -49, -32, -40, 48, 20, -27, -22, -1, -20, -5, 29, 18, -28, -36])) # [35, -47, -15, 28, 29, -40, -43, -25, -32, 57, 30, -16, -10, 12, -6, 10, 45, 35, -10, -17]
print(add_indexes([-48])) # [-48]
print(add_indexes([-15, -20, -28, -41, -2, -36, -18, -23, 44, -17, -12, -33, 7, 34, 5, -16])) # [-15, -19, -26, -38, 2, -31, -12, -16, 52, -8, -2, -22, 19, 47, 19, -1]
print(add_indexes([-20, 25, 49, -4, -20, -26, 23, 23, -50, 44, -48, -27])) # [-20, 26, 51, -1, -16, -21, 29, 30, -42, 53, -38, -16]
print(add_indexes([-9, 46, -17, 26, 0, -26, 12, -15, -30, -44, 29, 45, -38, -43])) # [-9, 47, -15, 29, 4, -21, 18, -8, -22, -35, 39, 56, -26, -30]
print((add_indexes([-44, -42, 26, -50, -29, -32, -22, 27, -31, 21, -12, -18, -13, -24, 24, 35])) # [-44, -41, 28, -47, -25, -27, -16, 34, -23, 30, -2, -7, -1, -11, 38, 50]
print(add_indexes([49, -28, -30, 35])) # [49, -27, -28, 38]
print(add_indexes([20, -5, 25, -36, -12, 13, -30, 26, 34]) # [20, -4, 27, -33, -8, 18, -24, 33, 42]
print(add_indexes([-41, -22, -41, -12])) # [-41, -21, -39, -9]
print(add_indexes([-23, 26, 22]) # [-23, 27, 24]
print(add_indexes([-5, 25, 19, 31, -39, 26, 4, 10, -43, -4, 26, -34, -1, -13, -26, -45]) # [-5, 26, 21, 34, -35, 31, 10, 17, -35, 5, 36, -23, 11, 0, -12, -30]
print(add_indexes([48, -6, 13, 39]) # [48, -5, 15, 42]
print(add_indexes([18, 27, -27, -35, -19, -5, -37, 20])) # [48, -5, 15, 42]
print(add_indexes([18, 27, -27, -35, -19, -5, -37, 20])) # [18, 28, -25, -32, -15, 0, -31, 27]
print(add_indexes([-26, 37, -29, -35, 18, 20, -25])) # [18, 28, -25, -32, -15, 0, -31, 27]
print(add_indexes([-26, 37, -29, -35, 18, 20, -25])) # [-26, 38, -27, -32, 22, 25, -19]
print(add_indexes([-49, 33, -7, -25])) # [-49, 34, -5, -22]
print(add_indexes([8, -21, -1, -46, 2, 48, -14, 45, 7, 12, 9, 45, -12, -8])) # [8, -20, 1, -43, 6, 53, -8, 52, 15, 21, 19, 56, 0, 5]
print(add_indexes([1, -12, 17, 12])) # [1, -11, 19, 15]
print(add_indexes([49, 9, 11, -18, -15, -23, 32, 44, 33])) # [49, 10, 13, -15, -11, -18, 38, 51, 41]
print(add_indexes([22, -50, 36, 12, 2, -48, 2, -21, -49, -47])) # [22, -49, 38, 15, 6, -43, 8, -14, -41, -38]
print(add_indexes([-44, 6, 16, -35, -30])) # [-44, 7, 18, -32, -26]
print([40, -38, -17, 24, -41, 43, -34, 11, -38, -42, -1, 16, 20])) # [40, -37, -15, 27, -37, 48, -28, 18, -30, -33, 9, 27, 32]
print(add_indexes([-31, -5, -5])) # [-31, -4, -3]
print(add_indexes([-44, 11, 26, 40, 3, 50, 3, 42, -1, 40, -12, 48, 0, 18, 1, -28, -18, 47, 45, 2])) # [-44, 12, 28, 43, 7, 55, 9, 49, 7, 49, -2, 59, 12, 31, 15, -13, -2, 64, 63, 21, 22]
print(add_indexes([21, -10, -49])) # [21, -9, -47]
print(add_indexes([-45, 49, 6, -50, 12, -30, 36, -36, -3, -28, 7, -47, -24, 34, 39, 45, 25])) # [-45, 50, 8, -47, 16, -25, 42, -29, 5, -19, 17, -36, -12, 47, 53, 60, 41] 
print(add_indexes([-4, 45])) # [-4, 46]