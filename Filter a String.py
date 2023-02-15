def filter_string(txt):
    capitals = []
    tiny = []
    numnum = []
    others = []
    for x in txt:
        if x.isupper() == True:
            capitals.append(x)
        elif x.islower() == True:
            tiny.append(x)
        elif x.isnumeric() == True:
            numnum.append(x)
        else:
            others.append(x)
    return [len(capitals), len(tiny), len(numnum), len(others)]        
        
        
        
        
