def automorphic(n):
    automorphic_number = str(n * n)
    return automorphic_number.endswith(str(n))
    


assert automorphic(1) == True

assert automorphic(3) == False
# 3^2 = 9

assert automorphic(6) == True
# 6^2 = 36 (ends with 6)

assert automorphic(95) == False
# 95^2 = 9025 (does not end with 95)
