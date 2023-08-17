def nth_smallest(lst, n):
    if n > len(lst):
        return None
    else:
        lst.sort()
        return lst[n-1]

print(nth_smallest([1, 3, 5, 7], 1)) # 1
print(nth_smallest([1, 3, 5, 7], 3)) # 5
print(nth_smallest([1, 3, 5, 7], 5)) # None
print(nth_smallest([7, 3, 5, 1], 2)) # 3