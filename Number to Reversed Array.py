def reverse_list(num):
    lst_num = list(str(num))
    rev = [eval(i) for i in lst_num]
    return rev[::-1]
    

assert reverse_list(1485979) == [9, 7, 9, 5, 8, 4, 1]

assert reverse_list(623478) == [8, 7, 4, 3, 2, 6]

assert reverse_list(12345) == [5, 4, 3, 2, 1]

