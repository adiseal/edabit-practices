def balanced(lst):
    first_half_sum = sum(lst[:len(lst)//2])
    second_half_sum = sum(lst[len(lst)//2:])
    
    if first_half_sum == second_half_sum:
        return lst
    
    if first_half_sum > second_half_sum:
        lst[len(lst)//2:] = lst[:len(lst)//2]
    else:
        lst[:len(lst)//2] = lst[len(lst)//2:]
    
    return lst