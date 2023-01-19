def sort_nums_ascending(lst):
        return sorted(lst)
    
 
assert sort_nums_ascending([1, 2, 10, 50, 5]) == [1, 2, 5, 10, 50]

assert sort_nums_ascending([80, 29, 4, -95, -24, 85]) == [-95, -24, 4, 29, 80, 85]

assert sort_nums_ascending([]) == []