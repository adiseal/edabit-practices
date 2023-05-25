def invert(dct):
	d = {}
	for k,v in dct.items():
		d[v]=k
	return d
    
print(invert({ "z": "q", "w": "f" })) # { "q": "z", "f": "w" }