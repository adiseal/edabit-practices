def subset(lst1, lst2):
    a = set(lst1)
    count = 0
    for i in a:
        if i in lst2:
            count+= 1
            if count == len(a):
                return True
    else:
        return False