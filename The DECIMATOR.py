def DECIMATOR(txt):
    import math
    a = math.ceil(len(txt)/10)
    return txt[:len(txt)-a]
    
print(DECIMATOR("1234567890AB")) # "1234567890"