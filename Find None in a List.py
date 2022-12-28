def find_none(lst):
    if None in lst:
        return lst.index(None)
    return -1
    


assert find_none([1, 2, None]) == 2

assert find_none([None, 1, 2, 3, 4]) == 0

assert find_none([0, 1, 2, 3, 4]) == -1