def list_between(num1, num2, lst):
    length = len(lst) 
    new_lst = []
    for i in range(length):
        if lst[i] > num1 and lst[i] < num2:
            new_lst.append(lst[i]) 
    return new_lst
 
 
 
assert list_between(3, 8, [1, 5, 95, 0, 4, 7]) == [5, 4, 7]

assert list_between(1, 10, [1, 10, 25, 8, 11, 6]) == [8, 6]

assert list_between(7, 32, [1, 2, 3, 78]) == []