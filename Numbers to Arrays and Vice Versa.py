def to_list(num):
    b = []
    a = str(num)
    for i in a:
        b = b + [int(i)]
    return b

def to_number(lst):
    a = ""
    for i in lst:
        a = a + str(i)
    return int(a)
    
print(to_number([2, 3, 5])) # 235