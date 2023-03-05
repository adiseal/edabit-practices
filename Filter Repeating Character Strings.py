def identical_filter(lst):
    a  = []
    for i in lst:
        b = set(i)
        if len(b) == 1:
            a = a + [i]
    return a
    
print(identical_filter(["88", "999", "22", "545", "133"])) # ["88", "999", "22"]   