def divisible_by_left(n):    
    n = str(n)
    result = [False]
    for i in range(1, len(n)):
        if int(n[i-1]) != 0 and int(n[i]) % int(n[i-1]) == 0:
            result.append(True)
        else:
            result.append(False)
    return result