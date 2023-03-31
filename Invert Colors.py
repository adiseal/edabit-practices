def color_invert(rgb):
	a = []
	for i in rgb:
		a = a + [255-i]
	return tuple(a)
	
print(color_invert((165, 170, 221))) # (90, 85, 34)