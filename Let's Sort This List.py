def asc_des_none(lst, s):
    b =[]
    if s == "None":
        return lst
    lst.sort()
    if s == "Asc":
        return lst
    else:
        for i in lst:
            b = [i] + b
        return b
		
print(asc_des_none([7, 8, 11, 66], "Des")) # [66, 11, 8, 7]