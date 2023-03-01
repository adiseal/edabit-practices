def convert(data1, data2):
    a = type(data1)
    for x in data2:
        if a == tuple:
            return tuple(data2)
        elif a == list:
            return list(data2)
        elif a == set:
            return set(data2)
    return a
    
print(convert([1, 2, 4, 8], {2, 3, 5, 7, 11, 13}))