def is_in_order(txt):
    return txt == ''.join(sorted(txt))
    
print(is_in_order("abc")) # True
print(is_in_order("edabit")) # False
print(is_in_order("123")) # True
print(is_in_order("xyzz")) # True