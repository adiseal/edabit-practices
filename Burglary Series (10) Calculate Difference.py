def calc_diff(obj, limit):
	a = 0
	for x,y in obj.items():
		a = a + y
	return a - limit
    
print(calc_diff({ "baseball bat": 20 }, 5))