def squares_sum(n):
	return sum([i ** 2 for i in range(1, n + 1)])
    
    
assert squares_sum(3) == 14

assert squares_sum(12) == 650

assert squares_sum(13) == 819