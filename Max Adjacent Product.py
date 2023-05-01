def adjacent_product(lst):
    a = []
    for i in range(1,len(lst)):
        a = a + [lst[i]*lst[i-1]]
    return max(a)
    
print(adjacent_product([0, -1, 1, 24, 1, -4, 8, 10])) # 80