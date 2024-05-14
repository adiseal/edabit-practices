def is_positive_dominant(lst):
    unique_values = set(lst)
    pos_count = len([num for num in unique_values if num > 0])
    neg_count = len([num for num in unique_values if num < 0])
    
    return pos_count > neg_count