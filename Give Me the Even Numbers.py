def sum_even_nums_in_range(start, stop):
    stop += 1
    even = []
    for x in range(start, stop):
        if x % 2 == 0:
            even.append(x)
    return sum(even)
    
assert sum_even_nums_in_range(10, 20) == 90
# 10, 12, 14, 16, 18, 20

assert sum_even_nums_in_range(51, 150) == 5050

assert sum_even_nums_in_range(63, 97) == 1360