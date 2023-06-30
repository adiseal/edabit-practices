def animals(chickens, cows, pigs):
	totalLegs = (chickens * 2) + (cows * 4) + (pigs * 4)
	return totalLegs
    
print(animals(2, 3, 5)) # 36
print(animals(1, 2, 3)) # 22
print(animals(5, 2, 8)) # 50