def format_phone_number(lst):
    a = ""
    for i in lst:
        a = a + str(i)

    return "(" + a[0:3] + ")" +" "+ a[3:6] + "-" + a[6:]
    
print(format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8])) # "(519) 555-4468"