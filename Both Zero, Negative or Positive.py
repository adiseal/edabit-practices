def both(n1, n2):
    if (n1 < 0) and (n2 < 0): 
        return True
    elif (n1 > 0) and (n2 > 0):
        return True
    elif n1 == 0 and n2 == 0:
        return True
    else:
        return False
    

assert both(6, 2) == True

assert both(0, 0) == True

assert both(-1, 2) == False

assert both(0, 2) == False