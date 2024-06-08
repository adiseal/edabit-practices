from collections import Counter

def sum_common(lst1, lst2, lst3):
    counter1 = Counter(lst1)
    counter2 = Counter(lst2)
    counter3 = Counter(lst3)
    
    common_elements = counter1.keys() & counter2.keys() & counter3.keys()
    
    common_sum = 0
    for element in common_elements:
        min_count = min(counter1[element], counter2[element], counter3[element])
        common_sum += element * min_count
    
    return common_sum