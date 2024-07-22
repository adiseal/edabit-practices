def arrow(n):
    pattern = []
    
    for i in range(1, n + 1):
        pattern.append('>' * i)
    
    if n % 2 == 0:  
        pattern.append('>' * n)
    
    for i in range(n - 1, 0, -1):
        pattern.append('>' * i)
    
    return pattern