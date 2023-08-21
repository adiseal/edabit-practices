def remove_smallest(lst):
    if len(lst) == 0:
        return []
    else:
        lst.remove(min(lst))
        return lst

print(remove_smallest([1, 2, 3, 4, 5])) # [2, 3, 4, 5]
print(remove_smallest([5, 3, 2, 1, 4])) # [5, 3, 2, 4]
print(remove_smallest([2, 2, 1, 2, 1])) # [2, 2, 2, 1]