def is_truthy(val):
    if val != False and val != None and val != 0 and val != [] and val != {} and val != "":
        return 1
    else:
        return 0
        
        
assert is_truthy(0) == 0

assert is_truthy(False) == 0

assert is_truthy("") == 0

assert is_truthy("False") == 1