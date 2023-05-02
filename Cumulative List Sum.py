def cumulative_sum(lst):
	a = 0
	lis = []
	for i in lst:
		a = a + i
		lis = lis + [a]
	return lis
    
print(cumulative_sum([3, 3, -2, 408, 3, 3])) # [3, 6, 4, 412, 415, 418]