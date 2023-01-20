def second_largest(lst):
    lst_sort = sorted(lst)
    return lst_sort[-2]


assert second_largest([10, 40, 30, 20, 50]) == 40

assert second_largest([25, 143, 89, 13, 105]) == 105

assert second_largest([54, 23, 11, 17, 10]) == 23