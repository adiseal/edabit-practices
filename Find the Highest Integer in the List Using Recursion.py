def find_highest(lst):
	a = 0
	count  = -1
	for i in lst:
		count+=1
		if i>=a:
			a = i
		else:
			find_highest(lst[count+1:])
	return a
    
print(find_highest([-1, 3, 5, 6, 99, 12, 2])) # 99