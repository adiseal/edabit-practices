def min_swaps(s1: str, s2: str) -> int:
    count_01 = 0  
    count_10 = 0  
    
    for c1, c2 in zip(s1, s2):
        if c1 == '0' and c2 == '1':
            count_01 += 1
        elif c1 == '1' and c2 == '0':
            count_10 += 1

    return max(count_01, count_10)