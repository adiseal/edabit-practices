def is_first_superior(lst1, lst2):
    return lst1 > lst2
    


assert is_first_superior(["a", "d", "c"], ["a", "b", "c"]) == True

assert is_first_superior(["zebra", "ostrich", "whale"], ["ant", "ostrich", "whale"]) == True

assert is_first_superior([1, 2, 3, 4], [1, 2, 4, 4]) == False

assert is_first_superior([True, 10, "zebra"], [True, 10, "zebra"]) == False