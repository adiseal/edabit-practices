from itertools import combinations

def combo(lst, n):
    if n > len(lst):
        return []
    if n == 0:
        return [[]]
    return [list(c) for c in combinations(sorted(lst), n)]