def reverse_and_not(i):
    str_i = str(i)
    rev_i = str_i[::-1]
    return int(rev_i + str_i)
    
    
assert reverse_and_not(123) == 321123

assert reverse_and_not(152) == 251152

assert reverse_and_not(123456789) == 987654321123456789