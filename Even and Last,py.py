def even_last(lst):
    a = 0
    for i in range(0, len(lst),2):
        a = a + (lst[i] * lst[-1])
    return a
    
print(even_last([1, 3, 3, 1, 10])) # 140