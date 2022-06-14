# Author    : Adi Nugroho
# Date      : Jun/14/2022
# a function that takes a number and return a list of three numbers: 
# half of the number, quarter of the number and an eighth of the number

def half_quarter_eighth(n):
    lst = []
    half = n / 2
    quarter = n / 4
    eight = n / 8
    lst.append(half)
    lst.append(quarter)
    lst.append(eight)
    return lst
    
# print(half_quarter_eighth(6)) ➞ [3, 1.5, 0.75]