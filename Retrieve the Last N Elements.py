def last(lst, n):
    if n > len(lst):
        return "invalid"
    elif n == 0:
        return []
    else:
        return lst[-n:]

print(last([1, 2, 3, 4, 5], 1)) # [5]
print(last([4, 3, 9, 9, 7, 6], 3)) # [9, 7, 6]