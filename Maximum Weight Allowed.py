def weight_allowed(car, p, max_weight):
    max_weight_pound = max_weight / 0.453592
    passengers_weight = sum(p)
    combined = car + passengers_weight
    is_allowed = combined < max_weight_pound
    return is_allowed

#print(weight_allowed(3000, [150, 201, 75, 88, 195], 1700))
assert weight_allowed(3000, [150, 201, 75, 88, 195], 1700) == True
assert weight_allowed(3200, [220, 101, 115, 228, 15], 1700) == False
assert weight_allowed(2900, [225, 171, 300, 274, 191], 1850) == True