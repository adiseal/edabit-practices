def major_sum(lst):
    positive_sum = sum(x for x in lst if x > 0)    
    negative_sum = sum(x for x in lst if x < 0)
    zeros_count = lst.count(0)
    if abs(positive_sum) >= abs(negative_sum) and abs(positive_sum) >= zeros_count:
        return positive_sum
    elif abs(negative_sum) > abs(positive_sum) and abs(negative_sum) >= zeros_count:
        return negative_sum
    else:
        return zeros_count