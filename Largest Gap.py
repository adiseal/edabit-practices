def largest_gap(lst):
    sorted_lst = sorted(lst)
    max_gap = 0
    for i in range(1, len(sorted_lst)):
        gap = sorted_lst[i] - sorted_lst[i-1]
        if gap > max_gap:
            max_gap = gap
    return max_gap