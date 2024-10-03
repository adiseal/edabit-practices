def is_anti_list(lst1, lst2):
    # Check if both lists have the same length
    if len(lst1) != len(lst2):
        return False
    
    # Identify the two unique elements in the first list
    unique_elements = set(lst1)
    
    # If there are not exactly two unique elements, return False
    if len(unique_elements) != 2:
        return False
    
    # Create a mapping of element pairs from lst1 to lst2
    elem1, elem2 = unique_elements
    for a, b in zip(lst1, lst2):
        # Check if a == elem1 implies b == elem2, and a == elem2 implies b == elem1
        if (a == elem1 and b != elem2) or (a == elem2 and b != elem1):
            return False
    
    return True
