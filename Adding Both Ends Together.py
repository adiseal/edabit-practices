def ends_add_to_10(lst):
    count = 0
    for num in lst:
        num = str(abs(num))  
        if int(num[0]) + int(num[-1]) == 10:  
            count += 1
    return count