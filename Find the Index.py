def find_index(lst, txt):
    index = lst.index(txt)
    return index
    

assert find_index(["hi", "edabit", "fgh", "abc"], "fgh") == 2

assert find_index(["Red", "blue", "Blue", "Green"], "blue") == 1

assert find_index(["a", "g", "y", "d"], "d") == 3

assert find_index(["Pineapple", "Orange", "Grape", "Apple"], "Pineapple") == 0