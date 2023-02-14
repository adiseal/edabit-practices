def binary_to_decimal(lst):
	number = 0
	for i in lst:
		number = (2 * number) + i
	return number
    
assert binary_to_decimal([0, 0, 0, 1]) == 1

assert binary_to_decimal([0, 0, 1, 0]) == 2

assert binary_to_decimal([1, 1, 1, 1, 1, 0, 1, 1, 0, 1]) == 1005