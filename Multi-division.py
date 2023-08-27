def abcmath(a, b, c):
    for i in range(b):
        a += a
    return a % c == 0

print(abcmath(42, 5, 10)) # False
print(abcmath(5, 2, 1)) # True