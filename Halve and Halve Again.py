def halve_count(a, b):
    count = 0
    while a > b:
        a /= 2
        count += 1
    return count - 1

print(halve_count(1324, 98)) # 3
print(halve_count(624, 8)) # 6
print(halve_count(1000, 3)) # 8