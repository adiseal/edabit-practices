def find_odd(lst):
    for i in lst:
        if lst.count(i) % 2 != 0:
            return i
            
print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])) # -1