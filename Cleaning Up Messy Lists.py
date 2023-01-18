def clean_up_list(lst):
    odd = []
    even = []
    combine = [even]+ [odd]
    for i in lst:
        if int(i) % 2 == 0:
            even.append(int(i))
        else:
            odd.append(int(i))
    return combine
    

  
assert clean_up_list(["8"]) == [[8], []]

assert clean_up_list(["11"]) == [[], [11]]

assert clean_up_list(["7", "4", "8"]) == [[4, 8], [7]]

assert clean_up_list(["9", "4", "5", "8"]) == [[4, 8], [9, 5]]