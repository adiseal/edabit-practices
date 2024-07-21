def is_legitimate(pool):
    if 1 in pool[0] or 1 in pool[-1]:
        return False
    
    for row in pool:
        if row[0] == 1 or row[-1] == 1:
            return False
    
    return True