def tuck_in(lst1, lst2):
    return [lst1[0]] + lst2 + [lst1[1]]

print(tuck_in([1, 10], [2, 3, 4, 5, 6, 7, 8, 9])) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]