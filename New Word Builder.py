def word_builder(ltr, pos):
	a = []
	for i in pos:
		a+=ltr[i]
	return "".join(a)
    
print(word_builder(["e", "t", "s", "t"], [3, 0, 2, 1])) # "test"