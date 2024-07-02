def greater_than_sum(lst):
    for i in range(1, len(lst)):
        if lst[i] <= sum(lst[:i]):
            return False
    return True