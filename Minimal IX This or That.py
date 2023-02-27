def first_one(a, b = None ,c = None, d = None):                             
	if bool(a) == True:
		return a
	elif bool(b) == True:
		return b
	elif bool(c) == True:
		return c
	elif bool(d) == True:
		return d
	else:
		return "not found"