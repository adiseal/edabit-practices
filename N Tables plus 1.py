def n_tables_plus_one(num):
    plus_one = []
    multiply = 1
    for x in range(num, num+10):
        plus_one.append(num * multiply + 1)
        multiply += 1
    listToStr = ",".join([str(elem) for elem in plus_one])
    return listToStr
    
    
assert n_tables_plus_one(7) == "8,15,22,29,36,43,50,57,64,71"

assert n_tables_plus_one(1) == "2,3,4,5,6,7,8,9,10,11"

assert n_tables_plus_one(3) == "4,7,10,13,16,19,22,25,28,31"