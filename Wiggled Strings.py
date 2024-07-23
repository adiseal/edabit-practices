def wiggle_string(s):
    result = []
    n = len(s)    
    for i in range(n + 1):
        result.append(' ' * i + s)    
    for i in range(n - 1, -1, -1):
        result.append(' ' * i + s)
    
    return result