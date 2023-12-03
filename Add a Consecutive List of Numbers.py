def add_up_to(n):
    sum_of_n = []
    for x in range(1, n+1):
        sum_of_n.append(x)
    return sum(sum_of_n)

print(add_up_to(3)) # 6
print(add_up_to(10)) # 55
print(add_up_to(0)) # 0
print(add_up_to(7)) # 28
print(add_up_to(2)) # 3
print(add_up_to(20)) # 210
print(add_up_to(1)) # 1