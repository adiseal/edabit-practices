def merge_sort(list1, list2):
    # Merge the two lists
    merged_list = list1 + list2
    # Check the order of the first list
    if list1 == sorted(list1):
        # If the first list is in ascending order, sort the merged list in ascending order
        return sorted(merged_list)
    else:
        # If the first list is in descending order, sort the merged list in descending order
        return sorted(merged_list, reverse=True)
