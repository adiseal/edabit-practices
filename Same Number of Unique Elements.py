def same(a1, a2):
    return len(set(a1)) == len(set(a2))


assert same([1, 3, 4, 4, 4], [2, 5, 7]) == True

assert same([9, 8, 7, 6], [4, 4, 3, 1]) == False

assert same([2], [3, 3, 3, 3, 3]) == True