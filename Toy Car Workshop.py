def cars(wheels, bodies, figures):
	a = [int(wheels/4),int(bodies/1),int(figures/2)]
	return min(a)
    
print(cars(43, 15, 87)) # 10