def sum_missing_numbers(lst):
    min_val = min(lst)
    max_val = max(lst)
    full_range = set(range(min_val, max_val + 1))
    missing_numbers = full_range - set(lst)
    return sum(missing_numbers)
