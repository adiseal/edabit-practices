def multiply_by_length(arr):
	a = []
	for i in arr:
		a = a + [i*len(arr)]
	return a
    
print(multiply_by_length([1, 0, 3, 3, 7, 2, 1])) # [7, 0, 21, 21, 49, 14, 7]