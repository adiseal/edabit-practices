def percent_filled(box):
    total = 0
    filled = 0
    for row in box[1:-1]:  
        for char in row[1:-1]:  
            if char == ' ':
                total += 1
            elif char == 'o':
                total += 1
                filled += 1
    return str(round((filled / total) * 100)) + '%'