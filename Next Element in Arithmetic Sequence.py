def next_element(lst):
    next_seq = lst[1] - lst[0]
    return lst[-1] + next_seq

assert next_element([3, 5, 7, 9]) == 11

assert next_element([-5, -6, -7]) == -8

assert next_element([2, 2, 2, 2, 2]) == 2