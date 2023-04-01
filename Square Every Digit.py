def square_digits(n):
    a = str(n)
    b = ""
    for i in a:
        b = b + str((int(i)*int(i)))
    return int(b)
    
print(square_digits(2483)) # 416649