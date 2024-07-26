def euclidean(a, b):
    if a < b:
        a, b = b, a
    
    if b == 0:
        return a
    
    return euclidean(b, a % b)