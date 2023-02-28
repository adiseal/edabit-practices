def lonely_integer(lst):
    for x in lst:
        if -x not in lst:
            return x
    
print(lonely_integer([-9, -105, -9, -9, -9, -9, 105])) #➞ -9