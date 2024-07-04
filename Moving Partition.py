def moving_partition(lst):
    if not lst:
        return []
    result = []
    for i in range(len(lst) - 1):
        result.append([lst[:i+1], lst[i+1:]])
    return result