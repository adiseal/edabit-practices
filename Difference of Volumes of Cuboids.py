def find_difference(a, b):
    result1 = 1
    result2 = 1
    
    # Multiply elements one by one
    for x in a:
        result1 *= x     
    # Multiply elements one by one
    for y in b:
        result2 *= y 
    
    if result1 > result2:
        return result1 - result2
    return result2 - result1


assert find_difference([ 28, 16, 29 ], [ 7, 8, 17 ]) == 12040

assert find_difference([ 9, 22, 18 ], [ 16, 24, 10 ]) == 276

assert find_difference([ 1, 9, 25 ], [ 10, 7, 9 ]) == 405

assert find_difference([ 7, 6, 16 ], [ 26, 9, 26 ]) == 5412
