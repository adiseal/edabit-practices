def sum_found_indexes(lst, n):
    res_list = []
    for x in range(0, len(lst)):
        if lst[x] == n:
            res_list.append(x)
    res = sum(res_list)
    return res
    
print(sum_found_indexes([100, 100, 100, 100, 100], 100))