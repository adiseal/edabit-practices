def antipodes_average(lst):
    # Step 1: Split the list into two equal parts
    n = len(lst)
    if n % 2 == 1:
        # If the list length is odd, remove the middle element
        lst.pop(n // 2)
        n -= 1
    
    # Split the list into two halves
    first_half = lst[:n // 2]
    second_half = lst[n // 2:]
    
    # Step 2: Sum each number of the first part with each number of the reversed second part
    second_half.reverse()
    summed_list = [first_half[i] + second_half[i] for i in range(n // 2)]
    
    # Step 3: Divide each number in the resulting list by two
    result = [x / 2 for x in summed_list]
    
    return result