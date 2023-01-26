def get_multiplied_list(lst):
    multiplied_result = []
    for i in lst:
        i *= 2
        multiplied_result.append(i)
    return multiplied_result
    
    
get_multiplied_list([2, 5, 3]) == [4, 10, 6]

get_multiplied_list([1, 86, -5]) == [2, 172, -10]

get_multiplied_list([5, 382, 0]) == [10, 764, 0]