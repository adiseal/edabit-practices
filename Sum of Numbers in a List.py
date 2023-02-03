# Import math Library
import math

def list_sum(lst):
    sum_lst = []
    for x in lst:
        if x % 2 == 0:
            sum_lst.append(x ** 2)
        else:
            sum_lst.append(math.sqrt(x))
    return round(sum(sum_lst), 2)        
            

assert list_sum([1, 3, 3, 1, 10]) == 105.46
assert list_sum([2, 3, 4, 5]) == 23.97
assert list_sum([1, 31, 3, 11, 0]) == 11.62   