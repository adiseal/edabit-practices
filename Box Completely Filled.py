def completely_filled(box):
    for row in box[1:-1]:  
        if any(char != '*' for char in row[1:-1]):  
            return False
    return True
