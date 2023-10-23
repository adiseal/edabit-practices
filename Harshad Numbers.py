def is_harshad(num):
	str_num = str(num)
	lst_num = [int(x) for x in str_num]
	return False if num == 0 else num % sum(lst_num) == 0