# Author    : Adi Nugroho
# Date      : Jun/14/2022
# a function which validates whether a bridge is safe to walk on (i.e. has no gaps in it to fall through)

def is_safe_bridge(s):
    if " " in s:
        return False
    return True
    
# print(is_safe_bridge("## ####")) ➞ False