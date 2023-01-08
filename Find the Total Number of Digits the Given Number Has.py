def find_digit_amount(num):
	return len(list(str(num)))
    
    
assert find_digit_amount(123) == 3

assert find_digit_amount(56) == 2

assert find_digit_amount(7154) == 4

assert find_digit_amount(61217311514) == 11

assert find_digit_amount(0) == 1