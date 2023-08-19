def sum_two_smallest_nums(lst):
    lst = [x for x in lst if x > 0]
    lst.sort()
    return lst[0] + lst[1]
