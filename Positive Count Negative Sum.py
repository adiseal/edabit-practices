def sum_neg(lst):
    if len(lst) == 0:
        return []
    index = 0
    output = []
    s = 0
    b = 0
    while index < len(lst):
        if lst[index] > 0:
            s += 1
        elif lst[index] <0:
            b += lst[index]
        index += 1
    output.append(s)
    output.append(b)
    return output
	
print(sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34])) # [7, -252]