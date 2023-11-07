def ranged_reversal(lst, start, end):
    return lst[:start] + lst[start:end+1][::-1] + lst[end+1:]

print(ranged_reversal([1, 2, 3, 4, 5, 6], 1, 3)) # [1, 4, 3, 2, 5, 6]