def mean(nums):
	return round(sum(nums) / len(nums), 1)
 

 
assert mean([1, 6, 6, 7, 8, 8, 9, 10, 10]) == 7.2

assert mean([1, 3, 8, 9, 9, 10]) == 6.7

assert mean([2, 3, 3, 6, 6, 8, 9, 10]) == 5.9