def move_to_end(lst, el):
    a = []
    for i in lst:
        if i != el:
            a = a + [i]
    b = lst.count(el)
    for i in range(b):
        a = a + [el]
    return a
    
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9)) # [7, 8, 1, 2, 3, 4, 9]