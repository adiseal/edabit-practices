def next_in_line(lst, num):
    if not lst:
        return "No list has been selected"
    else:
        lst.pop(0)
        lst.append(num)
        return lst
