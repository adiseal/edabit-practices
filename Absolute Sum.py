def get_abs_sum(lst):
    return sum(abs(num) for num in lst)
    
print(get_abs_sum([2, -1, 4, 8, 10])) # 25