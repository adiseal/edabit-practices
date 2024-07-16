def replace(string, char_range):
    if not string:
        return ""
    
    start, end = char_range.split('-')
    result = []
    
    for char in string:
        if start <= char <= end:
            result.append('#')
        else:
            result.append(char)
    
    return ''.join(result)