def num_of_digits(num):
	num = str(num)
	new_num = num.replace("-", "")
	return len(str(new_num))
    
print(num_of_digits(12)) # 2