def to_number_list(lst):
    str_lst = [eval(i) for i in lst]
    return str_lst
 
 
assert to_number_list(["9.4", "4.2"]) == [9.4, 4.2]

assert to_number_list(["99", "20"]) == [99, 20]

assert to_number_list(["9.5", "8.8"]) == [9.5, 8.8]