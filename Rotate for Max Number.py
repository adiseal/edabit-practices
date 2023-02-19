def rotate_max_number(num):
    stri = ""
    stri_nums = str(num)
    list_nums = sorted(stri_nums, reverse=True)
    for x in list_nums:
        stri += x
    return int(stri)
    
print(rotate_max_number(1546))