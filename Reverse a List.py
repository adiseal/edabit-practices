def reverse(lst):
	return lst[::-1]
    
    
assert reverse([1, 2, 3, 4]) == [4, 3, 2, 1]

assert reverse([9, 9, 2, 3, 4]) == [4, 3, 2, 9, 9]

assert reverse([]) == []