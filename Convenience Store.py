def change_enough(change, amount_due):
    sums = 0
    index = 0
    while index < len(change):
        if index == 0:
            sums += change[index] * 0.25
        elif index == 1:
            sums += change[index] * 0.10
        elif index == 2:
            sums += change[index] * 0.05
        else:
            sums += change[index] * 0.01
        index += 1
    if sums >= amount_due:
        return True
    else:
        return False
	
print(change_enough([0, 0, 20, 5], 0.75)) # True