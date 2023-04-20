def get_discounts(nums, d):
	a  = []
	for i in nums:
		a = a + [(int(d[:-1])/100)*i]
	return a
    
print(get_discounts([10, 20, 40, 80], "75%")) # [7.5, 15, 30, 60]