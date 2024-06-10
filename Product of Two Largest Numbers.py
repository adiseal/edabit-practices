def product(lst):
    sorted_lst = sorted(lst, reverse=True)
    
    first_largest = sorted_lst[0]
    second_largest = None
    
    for num in sorted_lst:
        if num != first_largest:
            second_largest = num
            break
    
    if second_largest is None:
        second_largest = first_largest
    
    return first_largest * second_largest