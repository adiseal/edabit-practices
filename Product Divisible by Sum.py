def divisible(lst):
    product = 1
    total_sum = 0

    for num in lst:
        product *= num
        total_sum += num

    return product % total_sum == 0
	
print(divisible([3, 2, 4, 2])) # False