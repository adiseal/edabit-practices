def mirror(lst):
    a = lst
    b = []
    for x in lst[0:(len(lst) - 1)]:
        b = [x] + b
    return a + b
    
print(mirror([1, 2, 3, 4, 5])) #➞ [1, 2, 3, 4, 5, 4, 3, 2, 1]