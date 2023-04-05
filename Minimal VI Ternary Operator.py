def are_true(a,b):
	if a == True:
		return "both" if b == True else "first"
	elif b == True:
		return "second"
	else:
		return "neither"
        