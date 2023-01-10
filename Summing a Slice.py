def sum_first_n_nums(lst, n):
    if n == 0:
        return 0
    elif n > len(lst):
        return sum(lst)
    else:
        return sum(lst[0:n])


assert sum_first_n_nums([1, 3, 2], 2) == 4

assert sum_first_n_nums([4, 2, 5, 7], 4) == 18

assert sum_first_n_nums([3, 6, 2], 0) == 0