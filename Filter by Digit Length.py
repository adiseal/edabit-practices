def filter_digit_length(lst, num):
    lsting = []
    for x in lst:
        if len(str(x)) == num:
            lsting.append(x)
    return lsting


print(filter_digit_length([32, 88, 74, 91, 300, 4050], 1)) #➞ [232, 555])
	