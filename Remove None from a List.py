def remove_none(lst):
    new_lst = []
    for x in lst:
        if x != None:
            new_lst.append(x)
    return new_lst