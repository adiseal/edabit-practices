def remove_smallest(lst):
    if len(lst) == 0:
        return []
    else:
        lst.remove(min(lst))
        return lst

print(remove_smallest([1, 2, 3, 4, 5])) # [2, 3, 4, 5]