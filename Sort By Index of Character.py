def sort_by_character(lst, n):
    index = n - 1
    return sorted(lst, key=lambda x: x[index])