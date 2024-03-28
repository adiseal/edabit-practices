def intersection_union(list1, list2):
    set1, set2 = set(list1), set(list2)        
    intersection = sorted(list(set1 & set2))
    union = sorted(list(set1 | set2))
    return [intersection, union]