def largest_numbers(n, lst):
    lst = sorted(lst)
    print(lst)
    if n == 0:
        return []
    elif n == 1:
        return [lst[-1]]
    else:
        return lst[-n:]


assert largest_numbers(1, [7, 19, 4, 2]) == [19]

assert largest_numbers(3, [14, 12, 57, 11, 18, 16]) == [16, 18, 57]

assert largest_numbers(0, [1, 3, 4, 2]) == []
