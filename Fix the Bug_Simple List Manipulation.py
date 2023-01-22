def increment_items(lst):
    new_lst = []
    for i in lst:
        i += 1
        new_lst.append(i)
    return new_lst
    
    
assert increment_items([0, 1, 2, 3]) == [1, 2, 3, 4]

assert increment_items([2, 4, 6, 8]) == [3, 5, 7, 9]

assert increment_items([-1, -2, -3, -4]) == [0, -1, -2, -3]