def additive_inverse(lst):
    index = 0
    output = []
    while index < len(lst):
        s = lst[index] * -1
        output.append(s)
        index += 1
    return output

print(additive_inverse([5, -7, 8, 3])) # [-5, 7, -8, -3]
print(additive_inverse([1, 1, 1, 1, 1])) # [-1, -1, -1, -1, -1]