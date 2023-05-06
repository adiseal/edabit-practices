def number_len_sort(lst):
	p = 0
	count = -1
	while(p<len(lst)):
		for j in lst[:len(lst)-1]:
			count = count + 1
			if len(str(lst[count]))<=len(str(lst[count+1])):
				continue
			else:
				a = lst[count]
				lst[count] = lst[count+1]
				lst[count+1] = a
		count = -1
		p = p + 1
	return lst
    
print(number_len_sort([999, 421, 22, 990, 32])) # [22, 32, 999, 421, 990]