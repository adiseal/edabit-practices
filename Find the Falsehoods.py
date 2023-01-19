def find_the_falsehoods(lst):
    new_lst = []
    for i in lst:
        if i == 0 or i == () or i == [] or i == {} or i == "" or i == None:
            new_lst.append(i)
    return new_lst



assert find_the_falsehoods([0, 1, 2, 3]) == [0]

assert find_the_falsehoods(["", "a", "ab"]) 

assert find_the_falsehoods([None, 1, [], [0], 0]) == [None, [], 0]

assert find_the_falsehoods([]) == []

assert find_the_falsehoods([[]]) == [[]]

assert find_the_falsehoods([[[]]]) == []