def is_in_order(txt):
    return txt == ''.join(sorted(txt))
    
print(is_in_order("abc")) # True
