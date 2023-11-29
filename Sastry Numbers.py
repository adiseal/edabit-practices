def is_sastry(n):
    concat_num = int(str(n) + str(n+1))    
    if int(concat_num ** 0.5) ** 2 == concat_num:
        return True
    else:
        return False
