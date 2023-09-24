def how_many_missing(lst):
    if not lst:
        return 0
    else:
        return max(lst) - min(lst) + 1 - len(lst)


print(how_many_missing([1, 3])) # 1
print(how_many_missing([7, 10, 11, 12])) # 2
print(how_many_missing([1, 3, 5, 7, 9, 11])) # 5