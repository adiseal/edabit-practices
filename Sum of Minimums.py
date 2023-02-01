def sum_minimums(lst):
    sum_lst = []
    for rows in lst:
        sum_lst.append(min(rows))
    return(sum(sum_lst))

