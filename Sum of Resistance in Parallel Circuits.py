def parallel_resistance(resistors):
    total = 0
    for r in resistors:
        total += 1/r
    return round(1/total, 1)
    
print(parallel_resistance([6, 3])) # 2