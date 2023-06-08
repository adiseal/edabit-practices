def reverse_psychology(s="Do not do anything."):
	# DO NOT WRITE YOUR CODE HERE
	if s != "Do not do anything.":
		return "Do not " + s + "."
	else:
		return s

print(reverse_psychology("wash the dishes")) # "Do not wash the dishes."