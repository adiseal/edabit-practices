def parallel_resistance(resistors):
    total = 0
    for r in resistors:
        total += 1/r
    return round(1/total, 1)
    
print(parallel_resistance([6, 3])) # 2
print(parallel_resistance([10, 20, 10])) # 4
print(parallel_resistance([500, 500, 500])) # 166.6
print(parallel_resistance([6, 3, 6])) # 1.5
print(parallel_resistance([60, 30, 20])) # 10
print(parallel_resistance([16, 4])) # 3.2
print(parallel_resistance([20, 5])) # 4
print(parallel_resistance([500, 500, 500])) # 166.7