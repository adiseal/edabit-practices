def power_morphic(num):
    count = 0
    for k in range(2, 11):
        if str(num ** k).endswith(str(num)):
            count += 1
    
    if count == 9:
        return "Polymorphic"
    elif count == 4:
        return "Quadrimorphic"
    elif count == 2:
        return "Dimorphic"
    elif count == 1:
        return "Enamorphic"
    else:
        return "Amorphic"