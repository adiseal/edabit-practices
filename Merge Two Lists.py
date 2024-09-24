def merge_arrays(list1, list2):
    merged_list = []
    # Determine the length of the shorter list
    min_length = min(len(list1), len(list2))
    
    # Alternate elements from both lists for the length of the shorter one
    for i in range(min_length):
        merged_list.append(list1[i])
        merged_list.append(list2[i])
    
    # Append any remaining elements from the longer list
    if len(list1) > min_length:
        merged_list.extend(list1[min_length:])
    elif len(list2) > min_length:
        merged_list.extend(list2[min_length:])
    
    return merged_list