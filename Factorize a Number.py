def factorize(num):
    lst_factorize = []
    for x in range(1, num+1):
        if num % x == 0:
            lst_factorize.append(x)
    return lst_factorize
    
print(factorize(12)) #➞ [1, 2, 3, 4, 6, 12])