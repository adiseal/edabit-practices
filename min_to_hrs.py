def min_to_hrs(n):
	return str(n) + " menit = " + str(round(float(n / 60), 2))
    
print(min_to_hrs(375) + " jam")