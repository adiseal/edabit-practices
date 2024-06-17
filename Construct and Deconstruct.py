def construct_deconstruct(s):
    result = []
    
    for i in range(1, len(s) + 1):
        result.append(s[:i])
    
    for i in range(len(s) - 1, 0, -1):
        result.append(s[:i])
    
    return result