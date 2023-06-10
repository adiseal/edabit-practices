def pyramid_lists(n):
    result = []
    for i in range(1, n + 1):
        sublist = [i] * i
        result.append(sublist)
    return result
    
print(pyramid_lists(3)) # [[1], [2, 2], [3, 3, 3]]