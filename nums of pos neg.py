def pos_neg(lst):
    pos_count, neg_count = 0, 0
    for num in lst:
        if num >= 0:
            pos_count += 1
        else:
            neg_count += 1
    return "Positive: " + str(pos_count) + ", Negative: " + str(neg_count)
    
print(pos_neg([-9, -105, -9, -9, -9, -9, 105])) #➞ -4