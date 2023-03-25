def num_layers(n):
	return str((2**(n-1))/1000) + "m"
    
print(num_layers(4)) # "0.008m"