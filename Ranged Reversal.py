def ranged_reversal(lst, start, end):
    return lst[:start] + lst[start:end+1][::-1] + lst[end+1:]
