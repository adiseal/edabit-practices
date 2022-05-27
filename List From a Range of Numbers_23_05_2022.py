def range_of_num(start, end): 
    if start == end:
        return []
    start += 1     
    list = []   
    for i in range(start, end): 
        list.append(i)
        i += 1
    return list
    
# Example: range_of_num(2, 11) ➞ [3, 4, 5, 6, 7, 8, 9, 10]