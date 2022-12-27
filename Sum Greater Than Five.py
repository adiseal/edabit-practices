def sum_five(lst):
    new_lst = []
    for x in lst:
        if x > 5:
            new_lst.append(x)
            
    return sum(new_lst)   
        
        
    

assert sum_five([1, 5, 20, 30, 4, 9, 18]) == 77

assert sum_five([1, 2, 3, 4]) == 0

assert sum_five([10, 12, 28, 47, 55, 100]) == 252