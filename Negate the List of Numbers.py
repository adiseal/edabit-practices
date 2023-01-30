def negate(lst):
	return [-i for i in lst]
    
    
assert negate([1, 2, 3, 4]) == [-1, -2, -3, -4]

assert negate([-1, 2, -3, 4]) == [1, -2, 3, -4]

assert negate([]) == []