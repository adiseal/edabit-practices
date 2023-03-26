def filter_list(l):
	a = []
	for i in l:
		if type(i) == int:
			a = a + [i]
	return a
	
print(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"])) # [0, 1729]