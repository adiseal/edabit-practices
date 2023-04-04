def is_subset(lst1, lst2):
    for i in lst1:
        if i not in lst2:
            return False
    else:
        return True
        
print(is_subset([1, 2], [3, 5, 9, 1])) # False