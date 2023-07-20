def next_in_line(lst, num):
    if not lst:
        return "No list has been selected"
    else:
        lst.pop(0)
        lst.append(num)
        return lst

print(next_in_line([5, 6, 7, 8, 9], 1)) # [6, 7, 8, 9, 1]
print(next_in_line([7, 6, 3, 23, 17], 10)) # [6, 3, 23, 17, 10]
print(next_in_line([1, 10, 20, 42 ], 6)) # [10, 20, 42, 6]
print(next_in_line([], 6)) # "No list has been selected"