def mapping(letters):
	d = {}
	for i in letters:
		d[i] = i.upper()
	return d
    
print(mapping(["a", "v", "y", "z"])) # { "a": "A", "v": "V", "y": "Y", "z": "Z" }