def sum_missing_numbers(lst):
    start, end = min(lst), max(lst)
    return sum(range(start, end + 1)) - sum(lst)
