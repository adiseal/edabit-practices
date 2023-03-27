def probability(lst, n):
	count = 0
	for i in lst:
		if i >= n:
			count = count + 1
	return round(100 * (count / len(lst)), 1)
    
print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6)) # 70.0
