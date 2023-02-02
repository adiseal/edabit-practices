def add_up_to(n):
    sum_of_n = []
    for x in range(1, n+1):
        sum_of_n.append(x)
    return sum(sum_of_n)

print(add_up_to(10))