def even_last(lst):
    if len(lst) == 0:
        return 0
    return sum(lst[0::2]) * lst[-1]



assert even_last([]) == 0

assert even_last([1, 3, 3, 1, 10]) == 140

assert even_last([-11, 3, 3, 1, 10]) == 20
