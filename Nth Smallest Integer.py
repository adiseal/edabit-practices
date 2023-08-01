def nth_smallest(lst, n):
    if n > len(lst):
        return None
    else:
        lst.sort()
        return lst[n-1]
